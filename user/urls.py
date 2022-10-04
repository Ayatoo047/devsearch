from django.urls import path
from . import views

urlpatterns = [
    path('', views.usersprofile, name = 'home'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('edit-account/', views.editAccount, name='editprofile'),
    path('login/', views.loginPage, name='login'),     
    path('logout/', views.logoutuser, name='logout'),      
    path('register/', views.registeruser, name='register'),      
    path('account/', views.account, name='account'),      
    path('inbox/', views.inbox, name='inbox'),      
    path('create-skill/', views.createSkill, name='createskill'),      
    path('message/<str:pk>', views.dm, name='message'),      
    path('create-message/<str:pk>', views.createMessage, name='createmessage'),      
    path('update-skill/<str:pk>', views.updateSkill, name='updateskill'),      
    path('delete-skill/<str:pk>', views.deleteSkill, name='deleteskill'),
        ]