# Generated by Django 5.1.6 on 2025-02-25 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sales_app", "0002_bill_product_remove_customer_color_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Product_type",
            new_name="Producttype",
        ),
        migrations.AlterModelOptions(
            name="customer",
            options={
                "ordering": ["first_name"],
                "verbose_name": "Customer",
                "verbose_name_plural": "Customers sers",
            },
        ),
        migrations.AlterField(
            model_name="customer",
            name="first_name",
            field=models.CharField(
                help_text="max- 30 letters are allowed", max_length=30
            ),
        ),
    ]
