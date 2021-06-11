from django.shortcuts import redirect, render
from . import models

# Create your views here.
def index(request):
    return render(request, "index.html", locals())

def contact(request):
    is_contact = True
    return render(request, "contact.html", locals())

def contactdetail(request):
    return render(request, "contact-detail.html", locals())

def inscription(request):
    return render(request, "inscription.html", locals())

def updatecontact(request):
    return render(request, "update-contact.html", locals())

def addcontact(request):
    return render(request, "add-contact.html", locals())

def profil(request):
    return render(request, "profil.html", locals())