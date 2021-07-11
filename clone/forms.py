from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegistratinForm(forms.ModelForm):
    password = forms.CharField(label ='Password',
                                widget = forms.PasswordInput)

    password2 =forms.CharField(label='Repeat Password',
                                widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = ('username' , 'first_name' , 'email')    
    
    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords dont match')
    
        return cd['password2']
            