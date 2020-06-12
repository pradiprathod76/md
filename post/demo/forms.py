from django import forms
from .models import Post,Category,Audio

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['name','email','password','cover','sub']


class CgForm(forms.ModelForm):
            class Meta:
                model = Category
                fields = ['img','name','des']

class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['name','des','img','audio','cg','sub']
