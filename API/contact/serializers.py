from rest_framework import serializers
from contact import models

class UtilisateurSerializer(serializers.HyperlinkedModelSerializer) :
	class Meta :
		model = models.Utilisateur
		fields = '__all__'

class ContactSerializer(serializers.HyperlinkedModelSerializer) :
	class Meta :
		model = models.Contact
		fields = '__all__'

