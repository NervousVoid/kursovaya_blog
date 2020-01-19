from django import forms


class PostForm(forms.Form):
    name = forms.CharField(max_length=128, required=True)
    description = forms.CharField(max_length=512, required=True)
    text = forms.CharField(max_length=100000, required=True)
