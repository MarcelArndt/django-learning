from django.contrib import admin
from .models import Customer, Product, Bill, Order, Producttype
# Register your models here.

class Customer_admin(admin.ModelAdmin):
    list_filter=['first_name', 'last_name', 'newsletter_abo', 'email_address', 'account']
    readonly_fields=['account']

admin.site.register(Customer, Customer_admin)
admin.site.register(Product)
admin.site.register(Bill)
admin.site.register(Order)
admin.site.register(Producttype)