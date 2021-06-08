from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), # <- here we have added the new path
    path('main_page/', views.Main.as_view(), name="main_page"),
    path('sign_up', views.Sign_up.as_view(), name="sign_up"),
]