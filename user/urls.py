from django.urls import path
from . import views

urlpatterns = [
    path('', views.usersprofile, name = 'home'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('login/', views.loginPage, name='login'),     
    path('logout/', views.logoutuser, name='logout'),      
    path('register/', views.registeruser, name='register'),      
    path('account/', views.account, name='account'),      
        ]