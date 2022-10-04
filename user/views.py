from contextvars import Context
import email
from pyexpat.errors import messages
from unicodedata import name
from django.shortcuts import redirect, render

from user.utils import searchProfile, paginateProject
from .models import Message, Profile
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .form import CustomUSerForm, MessageForm, SkillForm, ProfileForm
from . utils import searchProfile

# Create your views here.

def usersprofile(request):
    profiles, search_query = searchProfile(request)
    custom_range, profiles = paginateProject(request, profiles, 3)

    context = {'profiles': profiles, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'user/profiles.html', context)


def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    topskill = profile.skill_set.exclude(description__exact="")
    otherskill = profile.skill_set.filter(description="")

    context = {'profile': profile, 'topskill': topskill, 'otherskill': otherskill}
    return render(request, 'user/profile.html', context)


def loginPage(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)

        except:
            print('user doest not exist')

        user = authenticate(username = username, password = password)


        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')

        else:
            print('something went wrong')

    context = {'page': page}
    return render(request, 'user/login-register.html', context)


def logoutuser(request):
    logout(request)
    return redirect('login')


def registeruser(request):
    form = CustomUSerForm()
    if request.method == 'POST':
        form = CustomUSerForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
        
            return redirect('editprofile')
          
    context = {'form': form}
    return render(request, 'user/login-register.html', context)


def account(request):
    profile = request.user.profile
    # project = Profile.objects.get(id=pk)

    context = {'profile': profile}
    return render(request, 'user/account.html', context)


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {'form': form}
    return render(request, 'user/profile_form.html', context)


@login_required
def createSkill(request):
    profile = request.user.profile
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'project/create.html', context)


@login_required
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'project/create.html', context)


def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        return redirect('account')

    context = {"obj": skill}
    return render(request, 'project/delete.html', context)


def inbox(request):
    profile = request.user.profile
    userinbox = profile.messages.all()
    unreadNumber = userinbox.filter(is_read=False).count()
    context = {'userinbox': userinbox, 'unreadNumber': unreadNumber}
    return render(request, 'user/inbox.html', context)


def dm(request, pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()

    context = {'message': message, 'profile': profile}
    return render(request, 'user/message.html', context)


def createMessage(request, pk):
    recepient = Profile.objects.get(id=pk)
    form = MessageForm()

    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.receiver = recepient

            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()
            return redirect('profile', pk=recepient.id)
            
        
    context = {"recepient": recepient, 'form': form}
    return render(request, 'user/messageform.html', context)

