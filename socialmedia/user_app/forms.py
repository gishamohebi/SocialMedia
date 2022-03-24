from .models import *
from django import forms


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "image", "user", "text"]
        widgets = {  # in order to give css to the form's tags, we must name them
            'title': forms.TextInput(attrs={'class': 'title'}),
            'user': forms.Select(attrs={'class': 'user'}),
        }


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text", "user"]
