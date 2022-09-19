from multiprocessing import context
from re import search
from django.shortcuts import render, redirect
from project.utils import searchProject
from user.views import profile
from .models import Project, Tags
from . forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def projects(request):
    projects, search_query = searchProject(request)

    page = request.GET.get('page')
    results = 3
    paginator = Paginator(projects, results)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 2
        projects = paginator.page(page)


    projects = paginator.page(page)

    context = {'projects': projects, 'search_query': search_query}
    return render(request, 'project/projects.html', context)

def project(request, pk):
    project = Project.objects.get(id=pk)
    # tags = Tags.objects.all()
    context = {'project': project}
    return render(request, 'project/project.html', context)

def deleteproject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('home')

    context = {"obj": project}
    return render(request, 'project/delete.html', context)


@login_required
def createproject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'project/create.html', context)


@login_required
def updateproject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')

        else:
            print('theres an error during registration')
            
    context = {'form': form, 'project': project}
    return render(request, 'project/create.html', context)




