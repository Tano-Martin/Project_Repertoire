from django.db import models


# Create your models here.

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


