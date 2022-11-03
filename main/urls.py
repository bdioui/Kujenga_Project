"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.Index, name="Index"),
    path('test/', views.Home, name="Home"),
    path('test/contact/', views.Contact, name="Contact"),
    path('test/Portfolio/', views.Portfolio, name="Portfolio"),
    path('test/Team/', views.Team, name="Team"),
    path('test/projet/<int:pk>', views.Project, name="Project"),
    path('test/a-propos', views.A_propos, name="A_propos"),

    path('test/profile_Dania', views.Profile_Dania, name="Profile_Dania"),
    path('test/profile_Mambadi', views.Profile_Mambadi, name="Profile_Mambadi"),
    path('test/profile_Inou', views.Profile_Inou, name="Profile_Inou"),
    path('test/profile_Houza', views.Profile_Houza, name="Profile_Houza"),
]
