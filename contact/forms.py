from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreerUtilisateur(UserCreationForm):
    photo = forms.FileField(uploat_to="image")

    class Meta:
        model = User
        fields = ['username','photo', 'email', 'password1', 'password2']