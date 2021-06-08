from django.shortcuts import render
from django.views import View # <- View class to handle requests 
from django.http import HttpResponse # <- a class to handle sending a type of response  
from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


#import models
from .models import Photos

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = 'home.html'

@method_decorator(login_required, name='dispatch')
class Main(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["photos"] = Photos.objects.filter(
                name_icontains=name, user=self.request.user)
        else:
            context["photos"] = Photos.objects.filter(user=self.request.user)
        return context
        

class Signup(View):
    # show a form to fill out 
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form ssubmit validate the form and login the user. 
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("artist_list")
        else:
            return redirect("signup")
