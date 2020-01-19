from django import forms


class PostForm(forms.Form):
    name = forms.CharField(max_length=128, required=True)
    description = forms.CharField(max_length=512, required=True)
    text = forms.CharField(max_length=100000, required=True)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=32, required=True)
    password = forms.CharField(max_length=128, required=True)
    name = forms.CharField(max_length=32, required=True)
    surname = forms.CharField(max_length=32, required=True)
