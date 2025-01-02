from django.shortcuts import render,redirect
from django.http import HttpResponse


# Create your views here.


def homepage(request):
    return render(request,'home.html')

def servicepage(request):
    return render(request,'service.html')

def aboutpage(request):
    return render(request,'about.html')

def contactpage(request):
    return render(request,'contact.html')

def menupage(request):
    return render(request,'menu.html')



def contact_confirmation(request):
    return render(request,'confirmation.html')

