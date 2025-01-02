from django.urls import path
from . import views

urlpatterns=[
    path("",views.homepage),
    path("home",views.homepage),
    path("service",views.servicepage),
    path("about",views.aboutpage),
    path("contact",views.contactpage),
    path("menu",views.menupage),
    path("contact/confirmation/",views.contact_confirmation, name='contact_confirmation'),

   
   
]