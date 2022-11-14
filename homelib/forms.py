from django import forms
from .models import *
# from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class AddBook(forms.Form):
    title = forms.CharField(max_length=100)
    first_name_author = forms.CharField(max_length=50)
    last_name_author = forms.CharField(max_length=50)
    name_genre = forms.CharField(max_length=50)
    book_language = forms.CharField(max_length=50)
    book_image = forms.ImageField()


class AddFeedback(forms.Form):
    book_feedback = forms.CharField(widget=forms.Textarea())


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']

class LibRegistrationForm(forms.Form):
    library_name = forms.CharField(max_length=50)
    library_description = forms.CharField(max_length=300)
    library_contacts = forms.CharField(max_length=200)
    library_city = forms.CharField(max_length=50)
    library_image = forms.ImageField()
