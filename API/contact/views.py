from rest_framework import viewsets
from contact import models
from . import serializers

class UtilisateurViewSet(viewsets.ModelViewSet) :
	queryset = models.Utilisateur.objects.all()
	serializer_class = serializers.UtilisateurSerializer
	filterset_fields = ['date_add']

class ContactViewSet(viewsets.ModelViewSet) :
	queryset = models.Contact.objects.all()
	serializer_class = serializers.ContactSerializer
	filterset_fields = ['date_add']

