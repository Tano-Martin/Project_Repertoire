from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from . import models


class CompteUserForm(ModelForm):
    class Meta:
        models = models.CompteUser
        fields = '__all__'
        exclude = ['user']

class CreerUtilisateur(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ContactForm(ModelForm):
    class Meta:
        model = models.Contact
        fields = '__all__'