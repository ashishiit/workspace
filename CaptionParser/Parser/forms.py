'''
Created on Jul 26, 2018

@author: S528358
'''
# from django import forms
# from .models import Document
# 
# class DocumentForm(forms.ModelForm):
#     class Meta:
#         model = Document
#         fields = ('description', 'document', )

from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
#     file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))