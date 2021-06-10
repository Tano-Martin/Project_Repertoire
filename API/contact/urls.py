from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('Utilisateur', views.UtilisateurViewSet, basename='api-utilisateur')
router.register('Contact', views.ContactViewSet, basename='api-contact')
