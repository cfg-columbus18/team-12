from django import forms

class UserUpdate(forms.Form):
    username = forms.CharField(label='Username', max_length=191, required=False)