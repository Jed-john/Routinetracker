from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home (request):
    return render(request, 'routine_tracker_app/home.html')

def get_started(request):
    return render(request, 'routine_tracker_app/getstarted.html')

def onboarding(request):
    return render(request, 'routine_tracker_app/onboarding.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 != password2:
                error = 'Passwords do not match'
                form.add_error('password2', error)
            else:
                form.save()
                return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'routine_tracker_app/register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('myhome.html')  # Redirect to the home page after successful login
        
        else:
            error = 'Invalid username or password'
            messages.error(request, error)
    return render(request, 'routine_tracker_app/login.html')


def myhome (request):
    return render(request, 'routine_tracker_app/myhome.html')