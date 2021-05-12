"""todosProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import createTodos,list_todos,view_todos,delete_todo,update_todo
urlpatterns = [
   path('create',createTodos,name="createtodo"),
   path('list',list_todos,name="listtodo"),
   path('view/<int:id>',view_todos,name="viewtodo"),
   path('delete/<int:id>',delete_todo,name="deletetodo"),
   path('edit/<int:id>',update_todo,name="updatetodo")
]
