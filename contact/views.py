from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect, render
from . import models
from django.contrib import messages
from .forms import CompteUserForm, ContactForm, CreerUtilisateur
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    if request.method=='POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request, user)
            return redirect('contact', id_user=user)
        messages.error(request, "Erreur : information invalide.")
    return render(request, "index.html", locals())

def inscription(request):
    form = CreerUtilisateur()
    if request.method=='POST':
        form = CreerUtilisateur(request.POST)
        if form.is_valid():
            user = form.save()
            models.CompteUser.objects.create(user=user)
            
            # creation de groupe
            group = Group.objects.get(name='user_group')
            user.groups.add(group)
            return redirect('index')
    return render(request, "inscription.html", locals())


@login_required
def contact(request, id_user):
    is_contact = True
    user = get_object_or_404(User, username=id_user)
    return render(request, "contact.html", locals())

@login_required
def contactdetail(request, id_contact):
    contact = get_object_or_404(models.Contact, id=id_contact)
    return render(request, "contact-detail.html", locals())


@login_required
def updatecontact(request, id_contact):
    contact = get_object_or_404(models.Contact, id=id_contact)
    
    if request.method=='POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact.photo = form.cleaned_data["photo"]
            contact.nom = form.cleaned_data["nom"]
            contact.prenom = form.cleaned_data["prenom"]
            contact.email = form.cleaned_data["email"]
            contact.telephone = form.cleaned_data["telephone"]
            contact.save()
            return redirect('contact-detail', id_contact)
    else:
        form = ContactForm(initial={
            'photo': contact.photo,
            'nom': contact.nom,
            'prenom': contact.prenom,
            'email': contact.email,
            'telephone': contact.telephone,
        })
    return render(request, "update-contact.html", locals())

@login_required
def addcontact(request, id_user):
    
    if request.method=='POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.cleaned_data["photo"]
            nom = form.cleaned_data["nom"]
            prenom = form.cleaned_data["prenom"]
            email = form.cleaned_data["email"]
            telephone = form.cleaned_data["telephone"]
            contact = models.Contact(photo=photo, nom=nom, prenom=prenom, email=email, telephone=telephone, compteUser=request.user)
            contact.save()
            return redirect('contact', id_user)
    else :
        form = ContactForm()
    return render(request, "add-contact.html", locals())

@login_required
def profil(request):
    user = request.user
    form = CompteUserForm(instance=user)
    if request.method=='POST':
        form = CompteUserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
    return render(request, "profil.html", locals())

@login_required
def delete(request, id_contact):
    contact = models.Contact.objects.filter(id=id_contact)
    if contact :
        contact.delete()
    retour = request.META.get("HTTP_REFERER")
    return redirect(retour)

def logout_view(request):
    logout(request)
    return redirect('index')

