from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from . import models
from .forms import CreerUtilisateur


# Create your views here.
def index(request):
    
    if request.method=='POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password )
        if user is not None :
            login(request, user)
            return redirect('contact')
        
    return render(request, "index.html", locals())

def contact(request):
    is_contact = True
    return render(request, "contact.html", locals())

def contactdetail(request):
    return render(request, "contact-detail.html", locals())

def inscription(request):
    form = CreerUtilisateur()
    if request.method=='POST':
        form = CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, "inscription.html", locals())

def updatecontact(request):
    return render(request, "update-contact.html", locals())

def addcontact(request):
    return render(request, "add-contact.html", locals())

def profil(request):
    return render(request, "profil.html", locals())



# def inscriptionuser(request):
#     form = CreerUtilisateur()
#     if request.method=='POST':
#         form = CreerUtilisateur(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     return render(request, 'inscrit.html', locals())