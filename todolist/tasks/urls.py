from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('myday/', views.myday, name='myday'),
    path('tasks/', views.tasks, name='tasks'),
    path('important/', views.important, name='important'),
    path('add-task/', views.add_task, name='add_task'),



]
