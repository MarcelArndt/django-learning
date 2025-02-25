from django.urls import path, include
from django.contrib import admin
from .views import CustomerListView, CustomerListSearchView, CustomerListDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CustomerListView.as_view()),
    path('<str:name>', CustomerListSearchView.as_view()),
    path('customer/<int:pk>/', CustomerListDetailView.as_view()),
]