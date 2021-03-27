from django import forms
from django.forms import ModelForm
from .models import request_text

class PostForm(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    content = forms.CharField(label='内容', widget=forms.Textarea())


class Infomation_Form(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    content = forms.CharField(label='内容', widget=forms.Textarea())


class Sample_Form(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    image = forms.ImageField(label='イメージ画像', required=False)


class List_Form(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    content = forms.CharField(label='内容', widget=forms.Textarea())
    image = forms.ImageField(label='イメージ画像', required=False)


from django.forms import ModelForm
from .models import request_text

class request_Form(ModelForm):
    class Meta:
        model = request_text
        fields = ['title', 'text', 'image','country']

