# Generated by Django 3.2.13 on 2022-07-04 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20220704_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='number',
            field=models.CharField(editable=False, max_length=32),
        ),
    ]
