from django import forms
from .models import WikiPost, WikiCategory


class WikiPostForm(forms.ModelForm):
    class Meta:
        model = WikiPost
        fields = ('title', 'category', 'content')


class EditWikiPostForm(forms.ModelForm):
    class Meta:
        model = WikiPost
        fields = ('title', 'category', 'content')


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = WikiCategory
        fields = ('name', 'image')
