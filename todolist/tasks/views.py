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
            user = User.objects.filter(UEmail=email, UPassword=password).first()
            if user:
                request.session['UserID'] = user.UserID  # Store UserID in session
                return redirect('myday')  # Redirect to 'myday' page
            else:
                messages.error(request, 'Username or Password incorrect')

    return render(request, 'login.html', {'form': form})


def home(request):
    return render(request, "home.html")


def myday(request):
    user_id = request.session.get('UserID')
    if user_id:
        today_tasks = Task.objects.filter(created_at=date.today(), UserID=user_id)
        tasks_page = TaskForm()
        return render(request, "myday.html", {'today_tasks': today_tasks, 'tasks_page': tasks_page})
    else:
        return HttpResponse('User not logged in')


def tasks(request):
    user_id = request.session.get('UserID')
    if user_id:
        all_tasks = Task.objects.filter(UserID=user_id)
        return render(request, "tasks.html", {'all_tasks': all_tasks})
    else:
        # Handle the case when the user is not logged in
        return redirect('login')


def important(request):
    user_id = request.session.get('UserID')
    if user_id:
        important_tasks = Task.objects.filter(UserID=user_id, Priority="High")
        return render(request, "important.html", {'important_tasks': important_tasks})
    else:
        # Handle the case when the user is not logged in
        return redirect('login')


def add_task(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form
            new_task.save()
            return render(request, "myday.html", {'form': form})

    return render(request, "add_task.html", {'form': form})




