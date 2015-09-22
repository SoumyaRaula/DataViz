"""
Author : Soumyaranjan
Email : soumya.raula@gmail.com
Created : 19 Sep 2015

"""
from django import forms
from models import UserDataUpload

class UserDataUploadForm(forms.ModelForm):
    class Meta:
        model = UserDataUpload