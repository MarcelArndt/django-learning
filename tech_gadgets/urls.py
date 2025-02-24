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

from django.urls import path
from .views import start_page_view, GadgetsView, RedirectGadgets, gadgets_int_view, tech_gadgets_tes_render_view,  Manafatcory, ManafatcoryRedirect

#<sting: <int: <slug: -> datatype von der Variable aus der Url -> danach folgt der name der Variable selbst -> gadgets_id oder gadgets_slug
urlpatterns = [
    path('gadgets/test', tech_gadgets_tes_render_view),
    path('', RedirectGadgets.as_view()),
    path('gadgets/',  GadgetsView.as_view()),
    path('gadgets/<int:gadgets_id>', RedirectGadgets.as_view()),
    path('gadgets/<slug:gadgets_slug>', GadgetsView.as_view(), name='gadgets_slug_url'),
    path('factory/<int:factory_id>', ManafatcoryRedirect.as_view()),
    path('factory/<slug:factory_slug>', Manafatcory.as_view(), name = 'factory_slug_url'),
    path('factory/post', Manafatcory.as_view()),
]