# Generated by Django 4.2 on 2025-02-14 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='customer_tel',
            new_name='customer_tell',
        ),
    ]
