from django import forms
from django.forms import ModelForm
from . models import Post,Comment

#############################################################################################################

class PostModelForm(forms.ModelForm):
    content= forms.CharField(label ='Whats on your mind ?',widget=forms.Textarea(attrs={'rows':2}))
    class Meta:
        model = Post
        fields = ('content','image',)

#############################################################################################################

class CommentModelForm(forms.ModelForm):
    body = forms.CharField(label = '',widget =forms.TextInput(attrs={'placeholder': 'Add a comment...'}))
    class Meta:
        model = Comment
        fields = ('body',)

#############################################################################################################