from django import forms
from django.forms import ModelForm
from .models import Profile


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name','last_name','dob','Bio','country','avatar')

