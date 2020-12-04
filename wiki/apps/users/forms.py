from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import Profile
from django.utils.safestring import mark_safe


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
#        fields = ['username', 'password1', 'password2']
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class UserDeleteForm(forms.Form):
    delete_checkbox = forms.BooleanField(label=mark_safe('Sei sicuro di voler procedere?'), required=True)
    def __init__(self, *args, **kwargs):
        super(UserDeleteForm, self).__init__(*args, **kwargs)
