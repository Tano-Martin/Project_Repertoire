from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect, render
from . import models
from django.contrib import messages
from .forms import CreerUtilisateur
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    
    if request.method=='POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request, user)
            messages.success(request, "Enregistrement effectué avec succès.")
            return redirect('contact', id_user=user)
        messages.error(request, "Erreur : information invalide.")
    return render(request, "index.html", locals())

def inscription(request):
    form = CreerUtilisateur()
    if request.method=='POST':
        form = CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, "inscription.html", locals())


@login_required
def contact(request, id_user):
    is_contact = True
    user = get_object_or_404(User, username=id_user)
    return render(request, "contact.html", locals())

@login_required
def contactdetail(request, id_contact):
    #user = get_object_or_404(User, username=id_user)
    contact = get_object_or_404(models.Contact, id=id_contact)
    return render(request, "contact-detail.html", locals())


@login_required
def updatecontact(request, id_contact):
    contact = get_object_or_404(models.Contact, id=id_contact)
    return render(request, "update-contact.html", locals())

@login_required
def addcontact(request):
    return render(request, "add-contact.html", locals())

@login_required
def profil(request, id_user):
    user = get_object_or_404(User, username=id_user)
    return render(request, "profil.html", locals())

def logout_view(request):
    logout(request)
    return redirect('index')

# def inscriptionuser(request):
#     form = CreerUtilisateur()
#     if request.method=='POST':
#         form = CreerUtilisateur(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     return render(request, 'inscrit.html', locals())