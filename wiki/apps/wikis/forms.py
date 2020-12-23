from django import forms
from .models import WikiPost, WikiCategory
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404


class AddWikiPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(AddWikiPostForm, self).__init__(*args, **kwargs)
        self.fields['collaborators'].queryset = User.objects.exclude(username=self.request.user).order_by("username")

    class Meta:
        model = WikiPost
        fields = ('title', 'category', 'collaborators', 'content')


class EditWikiPostForm(forms.ModelForm):

    class Meta:
        model = WikiPost
        fields = ('title', 'category', 'collaborators', 'content')

    def __init__(self, *args, **kwargs): 
        self.request = kwargs.pop('request', None)
        super(EditWikiPostForm, self).__init__(*args, **kwargs)
        self.fields['collaborators'].queryset = User.objects.exclude(username=self.instance.author).order_by("username")



class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = WikiCategory
        fields = ('name', 'image')
