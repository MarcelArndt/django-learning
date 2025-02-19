"""
URL configuration for first_django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from tech_gadgets.views import start_page_view
from django.shortcuts import redirect

def redirect_to_tech_gadgets(request):
    return redirect('tech_gadgets/', permanent=True)

urlpatterns = [
    path("", redirect_to_tech_gadgets),
    path('tech_gadgets/', include('tech_gadgets.urls')),
]
