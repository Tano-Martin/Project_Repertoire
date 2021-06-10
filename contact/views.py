from django.shortcuts import redirect, render
from . import models

# Create your views here.
def index(request):
    utilisateurs = models.Utilisateur.objects.filter(status=True)
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

def userconnecte(request):
    utilisateurs = models.Utilisateur.objects.filter(status=True)

    return render(request, 'index.html', locals())