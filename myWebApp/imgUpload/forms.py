from django import forms
class ImageUploadForms(forms.Form):
    image = forms.ImageField()