from django import forms

#DataFlair #Form
class SignUp(forms.Form):
    first_name = forms.CharField(initial = 'First Name', )
    last_name = forms.CharField()
    username = forms.CharField(initial = 'User Name', )
    email = forms.EmailField(help_text = 'write your email', )
    password = forms.CharField(widget = forms.PasswordInput)
    re_password = forms.CharField(help_text = 'renter your password', widget = forms.PasswordInput)