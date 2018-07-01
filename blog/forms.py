from django import forms
from .models import Comemnt

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'comment')