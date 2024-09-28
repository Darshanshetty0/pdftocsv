from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

class ImageUploadForm(forms.Form):
    image = forms.ImageField()


