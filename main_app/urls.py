from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), # <- here we have added the new path
    path('main_page/', views.Main.as_view(), name="main_page"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('accounts/edit_profile/', views.UserEditView.as_view(), name="edit_profile"),
    
    path('main_page/add_picture/', views.AddPicture.as_view(), name='add_picture'),
    
    path('main_page/<int:pk>/delete_picture', views.DeletePicture.as_view(), name="delete_picture"),

    path('accounts/edit_profile_page/', views.EditProfilePageView.as_view(), name='edit_profile_page')
]