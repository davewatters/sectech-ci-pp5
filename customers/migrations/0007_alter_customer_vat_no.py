# Generated by Django 3.2.13 on 2022-07-08 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_auto_20220708_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='vat_no',
            field=models.CharField(blank=True, default='', max_length=16, null=True),
        ),
    ]
