from django import forms
from .models import WikiPost, WikiCategory
from django.contrib.auth.models import User


class WikiPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(WikiPostForm, self).__init__(*args, **kwargs)
        self.fields['collaborators'].queryset = User.objects.exclude(username=self.request.user).order_by("username")

    class Meta:
        model = WikiPost
        fields = ('title', 'category', 'collaborators', 'content')


class EditWikiPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(EditWikiPostForm, self).__init__(*args, **kwargs)
        self.fields['collaborators'].queryset = User.objects.exclude(username=self.request.user).order_by("username")

    class Meta:
        model = WikiPost
        fields = ('title', 'category', 'collaborators', 'content')


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = WikiCategory
        fields = ('name', 'image')
