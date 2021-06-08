from django.shortcuts import render
from django.views import View # <- View class to handle requests 
from django.http import HttpResponse # <- a class to handle sending a type of response  
from django.views.generic.base import TemplateView

#import models
from .models import Photos

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = 'home.html'

class Main(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["photos"] = Photos.objects.all()
        return context

class Sign_up(TemplateView):
    template_name = 'sign_up.html'

