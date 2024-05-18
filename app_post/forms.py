from django.forms import ModelForm
from .models import Post
from django import forms

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image']
        # labels = {
        #     'title': '',
        #     'body': '',
        #     'image': ''
        # }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Dodaj tytuł...', 'class': 'rounded-lg w-full dark:bg-[#313338]'}),
            'body': forms.Textarea(attrs={'placeholder': 'Dodaj treść...', 'style': 'resize: none;', 'class': 'w-full rounded-lg outline-none border-white dark:bg-[#313338]'}),
            'image': forms.ClearableFileInput(attrs={'class': 'text-black dark:text-white'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].label = ''