from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('inscription/', views.inscription, name="inscription"),
    path('contact-detail/', views.contactdetail, name="contact-detail")
]

