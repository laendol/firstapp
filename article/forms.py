__author__ = 'alex'

from django.forms import ModelForm
from models import Comments

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']
