# Generated by Django 3.2.13 on 2022-07-08 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_auto_20220704_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='postcode',
            field=models.CharField(blank=True, default='', max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='vat_no',
            field=models.CharField(default='', max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer_product',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='customers.customer'),
        ),
        migrations.AlterField(
            model_name='customer_product',
            name='last_bill_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
