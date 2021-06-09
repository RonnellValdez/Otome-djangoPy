from django.db.models.base import Model
from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.views import View, generic # <- View class to handle requests 
from django.http import HttpResponse # <- a class to handle sending a type of response  
from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView
#import models
from .models import Photos, Profile

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = 'home.html'

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
            return redirect("/main_page/")
        else:
            return redirect("signup")

class UserEditView(UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/edit_profile.html'
    success_url = '/main_page/'

    def get_object(self):
        return self.request.user



class EditProfilePageView(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'twitch_url', 'youtube_url', 'discord']
    success_url = '/main_page/'

    def get_object(self):
        return self.request.user.profile

class AddPicture (CreateView):
    model = Photos
    fields = ['name', 'img']
    template_name = "add_picture.html"

        # This is our new method that will add the user into our submitted form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPicture, self).form_valid(form)

    success_url = '/main_page/'

class DeletePicture(DeleteView):
    model = Photos
    template_name = "delete_picture_confirm.html"
    success_url = '/main_page/'
    # reverse = '/main_page/'


    # def get_success_url(self):
    #     print(self.kwargs)
    #     return reverse('/main_page/')