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
    form_user = CreerUtilisateur()
    form_info = CompteUserForm()
    if request.method=='POST':
        form_user = CreerUtilisateur(request.POST)
        form_info = CompteUserForm(request.POST, request.FILES)
        
        if form_user.is_valid() and form_info.is_valid() :
            user = form_user.save()
            user.save()
            profil = form_info.save(commit=False)
            profil.user = user
            profil.save()
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
    photo_actuelle = contact.photo
    if request.method=='POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact.photo = form.cleaned_data["photo"]
            if contact.photo == "photo.png" :
                contact.photo = photo_actuelle
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
def delete(request, id_contact):
    contact = models.Contact.objects.filter(id=id_contact)
    if contact :
        contact.delete()
    retour = request.META.get("HTTP_REFERER")
    return redirect(retour)

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def profil(request, id_user):
    user = get_object_or_404(User, username=id_user)
    profil = models.CompteUser.objects.get(user=user)
    
    if request.method == 'POST' :
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        photo = request.FILES.get('photo')

        user.email = email
        user.save()

        profil.user = user
        profil.prenom = prenom
        profil.telephone = telephone

        if not photo :
            profil.photo = profil.photo
        else :
            profil.photo = photo
        profil.save()
        return redirect('profil', id_user)
    return render(request, "profil.html", locals())

