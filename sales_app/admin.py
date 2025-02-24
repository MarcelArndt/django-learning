from django.contrib import admin
from .models import Customer, Product, Bill, Order, Product_type
# Register your models here.


class Customer_admin(admin.ModelAdmin):
    list_filter=['first_name', 'second_name', 'newsletter_abo', 'email_address', 'account']
    readonly_fields=['account']

admin.site.register(Customer, Customer_admin)
admin.site.register(Product)
admin.site.register(Bill)
admin.site.register(Order)
admin.site.register(Product_type)