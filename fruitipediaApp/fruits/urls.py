"""
URL configuration for fruitipediaApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from fruitipediaApp.fruits import views

urlpatterns = (
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-fruit/', views.create_fruit, name='create_fruit'),
    path('<int:fruit_id>/', include([
        path('details-fruit/', views.details_fruit, name='details_fruit'),
        path('edit-fruit/', views.edit_fruit, name='edit_fruit'),
        path('delete-fruit/', views.delete_fruit, name='delete_fruit'),
    ])),
    path('create-category/', views.create_category, name='create_category'),
)
