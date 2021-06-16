from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . import models


class CompteUserForm(forms.ModelForm):
    class Meta:
        model = models.CompteUser
        fields = ['prenom', 'telephone', 'photo']
        

class CreerUtilisateur(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = '__all__'
        exclude = ['compteUser'] 

