from django import forms
from django.forms.widgets import Textarea

class PostForm(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    content = forms.CharField(label='内容',widget=forms.Textarea())
