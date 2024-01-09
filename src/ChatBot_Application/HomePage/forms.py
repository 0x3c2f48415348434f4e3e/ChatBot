# forms.py
from django import forms

class UserInputForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)





