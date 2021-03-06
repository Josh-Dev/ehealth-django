from django import forms
from django.contrib.auth.models import User
from ehealth_project.models import Page, UserProfile, Folder

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('age','gender','pic',)

class UserFinderForm(forms.ModelForm):
    username = forms.CharField(max_length=128, help_text="Please enter a username")

    class Meta:
        model = User
        fields = ('username',)
