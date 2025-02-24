from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=30, help_text='max- 30 letters are allowed')
    second_name = models.CharField(max_length=30)
    newsletter_abo = models.BooleanField(default=False)
    email_address = models.CharField(max_length=30, blank=True,default='max-musterman@web.de' )
    account = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name = 'Customer' #Reiter namen und Titlename im Adminpanel
        verbose_name_plural = 'Customers sers' #Django macht automatisch ein s dran - falls man es manuel bearbeiten will
        ordering=['first_name'] #wonach anfangs sotiert werden soll

    def __str__(self):
        return f"{self.first_name} {self.second_name}"

# Die Produke müssen nichgt wissen, wo in welcher Order sie drin sind.
class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} | {self.price}"


class Bill(models.Model):
    total_amount = models.FloatField()
    is_paid = models.BooleanField(default=False)

# Aber eine Order kann mehrere Produkte beinhalten und muss über diese bescheit wissen.
# (through='Product_type') Product_type da erst später deffiniert werden kann.
# Product_type dient als zwischenInformation
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='Product_type')
    bill = models.OneToOneField(Bill, on_delete=models.CASCADE)
    # many-to-one Customer
    # one-to-one Bill
    # many-to-many Product

class Product_type(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type_name = models.CharField(max_length=300)  

    def __str__(self):
        return f"{self.type_name}"

   