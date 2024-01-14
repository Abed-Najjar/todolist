from datetime import date
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from .forms import UserForm, ListForm, TaskForm, LoginForm
from .models import User, List, Task
from django.contrib import messages


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():  # Check if a user with the same username or email already exists
            form.save()
            return redirect('login')  # Replace with your login URL name
    else:
        form = UserForm()

    return render(request, 'signup.html', {'form': form})


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['UEmail']
            password = request.POST['UPassword']
            user = User.objects.get(UEmail=email)
            if User.objects.filter(UEmail=email).exists() and user.UEmail == email and user.UPassword == password:
                return render(request, "home.html")
            else:
                messages.error(request, 'Username or Password incorrect')

    return render(request, 'login.html', {'form': form})


def home(request):
    return render(request, "home.html")


def myday(request):
    today_tasks = Task.objects.filter(created_at=date.today(), UserID=3)    #add session value
    tasks_page = TaskForm()
    print(today_tasks)  # Print to console for debugging
    return render(request, "myday.html", {'today_tasks': today_tasks, 'tasks_page': tasks_page})


def tasks(request):
    all_tasks = Task.objects.filter(UserID=2)   #add session value
    print(all_tasks)  # Print to console for debugging
    return render(request, "tasks.html", {'all_tasks': all_tasks})


def important(request):
    important_tasks = Task.objects.filter(Priority="High")
    print(important_tasks)  # Print to console for debugging
    return render(request, "important.html", {'important_tasks': important_tasks})


