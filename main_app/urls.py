from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), # <- here we have added the new path
    path('main_page/', views.Main.as_view(), name="main_page"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
]