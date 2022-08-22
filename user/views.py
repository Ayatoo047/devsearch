from atexit import register
from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Profile, Skill
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .form import CustomUSerForm

# Create your views here.

def usersprofile(request):
    profiles = Profile.objects.all()

    context = {'profiles': profiles}
    return render(request, 'user/profiles.html', context)

@login_required
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
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)

        except:
            print('user doest not exist')

        user = authenticate(username = username, password = password)


        if user is not None:
            login(request, user)
            return redirect('home')

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
        
            return redirect('home')
          
    context = {'form': form}
    return render(request, 'user/login-register.html', context)


def account(request):
    profile = request.user.profile
    # project = Profile.objects.get(id=pk)

    context = {'profile': profile}
    return render(request, 'user/account.html', context)