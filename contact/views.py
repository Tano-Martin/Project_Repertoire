from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html", locals())

def contact(request):
    return render(request, "contact.html", locals())

def contactdetail(request):
    return render(request, "contact-detail.html", locals())

def inscription(request):
    return render(request, "inscription.html", locals())