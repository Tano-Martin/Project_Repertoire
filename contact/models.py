from django.db import models

# Create your models here.

class Utilisateur(models.Model):
	nom = models.CharField(max_length=255)
	prenom = models.CharField(max_length=255)
	photo = models.FileField(upload_to='Nom_file')
	email = models.EmailField()
	telephone = models.IntegerField(default=0)
	password = models.CharField(max_length=255)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Nom'
		verbose_name_plural = 'Noms'

	def __str__(self):
		return self.nom

class Contact(models.Model):
	nom = models.CharField(max_length=255)
	prenom = models.CharField(max_length=255)
	photo = models.FileField(upload_to='Contact_file')
	email = models.EmailField()
	telephone = models.IntegerField(default=0)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Contact'
		verbose_name_plural = 'Contacts'

	def __str__(self):
		return self.nom

