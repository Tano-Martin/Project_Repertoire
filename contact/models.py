from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CompteUser(models.Model):
	user = models.OneToOneField(User, related_name="compte", null=True, blank=True, on_delete=models.CASCADE)
	prenom = models.CharField(max_length=255, blank=True, null=True)
	photo = models.FileField(upload_to='CompteUser_file', default='photo.png', blank=True, null=True)
	telephone = models.IntegerField(default=0, blank=True, null=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'CompteUser'
		verbose_name_plural = 'CompteUsers'

	def __str__(self):
		return f"{self.user}"


class Contact(models.Model):
	nom = models.CharField(max_length=255)
	prenom = models.CharField(max_length=255, blank=True, null=True)
	photo = models.FileField(upload_to='Contact_file', default='photo.png' , blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	telephone = models.IntegerField(default=0)
	compteUser = models.ForeignKey(User, related_name="contact_user", on_delete=models.CASCADE, blank=True, null=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Contact'
		verbose_name_plural = 'Contacts'

	def __str__(self):
		return self.nom


