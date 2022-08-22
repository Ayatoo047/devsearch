from venv import create
from django.urls import path

from project import views
import project

urlpatterns = [
    path('projects/', views.projects, name="projects"),
    path('single-project/<str:pk>/', views.project, name='project'),
    path('delete-project/<str:pk>/', views.deleteproject, name='delete-project'),
    path('create-project/', views.createproject, name='create-project'),
    path('update-project/<str:pk>/', views.updateproject, name='update-project'),
]
