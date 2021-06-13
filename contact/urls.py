from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('logout/', views.logout_view, name="logout"),

    path('contact/<str:id_user>', views.contact, name="contact"),
    path('inscription/', views.inscription, name="inscription"),
    path('profil/<str:id_user>', views.profil, name="profil"),
    path('contact-detail/<int:id_contact>', views.contactdetail, name="contact-detail"),
    path('update-contact/<int:id_contact>', views.updatecontact, name="update-contact"),
    path('add-contact/', views.addcontact, name="add-contact"),


    # path('inscriptionuser/', views.inscriptionuser, name="inscriptionuser"),
 
]

