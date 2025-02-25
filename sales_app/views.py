from django.shortcuts import render
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Customer, Bill


class CustomerListView(ListView):
    model = Customer
    template_name = 'sales/list.html'

class CustomerListSearchView(CustomerListView):
    def get_queryset(self):
        name = self.kwargs.get('name')
        return Customer.objects.filter(first_name__icontains=name)
    
# die pk ist eine fortläufige nummer, die nicht nach dem löschen zurücksetzt wird  ... es sind die pk 4,5,6 und nicht 1,2,3
class CustomerListDetailView(DetailView):
    model = Customer
    template_name = 'sales/detail.html'
    
    def get_object(self):
        obj = super().get_object()
        obj.last_accessed = timezone.now()
        return obj
    