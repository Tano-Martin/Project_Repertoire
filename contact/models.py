from contact.views import contact
from django.db import models
from django import forms

# Create your models here.

class Utilisateur(models.Model):
	nom = models.CharField(max_length=255)
	prenom = models.CharField(max_length=255)
	photo = models.FileField(upload_to='Nom_file', blank=True, null=True)
	email = models.EmailField()
	telephone = models.IntegerField(default=0)
	password = models.CharField(max_length=255)
	contact = models.ManyToManyField('contact.contact', related_name='contact_user', blank=True, null=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Utilisateur'
		verbose_name_plural = 'Utilisateurs'

	def __str__(self):
		return self.nom

class Contact(models.Model):
	nom = models.CharField(max_length=255)
	prenom = models.CharField(max_length=255, blank=True, null=True)
	photo = models.FileField(upload_to='Contact_file', blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	telephone = models.IntegerField(default=0)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Contact'
		verbose_name_plural = 'Contacts'

	def __str__(self):
		return self.nom


