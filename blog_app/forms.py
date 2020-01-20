from django import forms


class PostForm(forms.Form):
    name = forms.CharField(label='Title', max_length=128, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=512, required=True,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(max_length=100000, required=True, widget=forms.Textarea(attrs={'class': 'form-control',
                                                                                           'rows': 10}))


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=32, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=128, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label='First name', max_length=32, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    surname = forms.CharField(label='Last name', max_length=32, required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))


class CommentForm(forms.Form):
    text = forms.CharField(label='Write a comment', max_length=100000, required=True,
                           widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
