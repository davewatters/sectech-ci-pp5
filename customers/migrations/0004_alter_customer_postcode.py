# Generated by Django 3.2.13 on 2022-06-30 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_customer_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='postcode',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
