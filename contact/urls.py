from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('inscription/', views.inscription, name="inscription"),
    path('profil/', views.profil, name="profil"),
    path('contact-detail/', views.contactdetail, name="contact-detail"),
    path('update-contact/', views.updatecontact, name="update-contact"),
    path('add-contact/', views.addcontact, name="add-contact"),


    # path('inscriptionuser/', views.inscriptionuser, name="inscriptionuser"),
 
]

