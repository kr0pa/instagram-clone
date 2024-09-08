from django.forms import ModelForm
from .models import Post
from django import forms

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image']
        # labels = {
        #     'title': 'Nazwa',
        #     'image': 'Wgraj'
        # }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Dodaj tytuł...', 'class': 'text-black dark:text-white rounded-lg w-full dark:bg-[#313338]'}),
            'body': forms.Textarea(attrs={'placeholder': 'Dodaj treść...', 'style': 'resize: none;', 'class': 'text-black dark:text-white w-full rounded-lg outline-none border-white dark:bg-[#313338]'}),
            'image': forms.ClearableFileInput(attrs={'class': 'text-black dark:text-white'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].label = ''
            
            
class EditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Dodaj tytuł...', 'class': 'text-black dark:text-white rounded-lg w-full dark:bg-[#313338]'}),
            'body': forms.Textarea(attrs={'placeholder': 'Dodaj treść...', 'style': 'resize: none;', 'class': 'text-black dark:text-white w-full rounded-lg outline-none border-white dark:bg-[#313338]'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].label = ''