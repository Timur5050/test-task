# Generated by Django 5.0.4 on 2024-05-22 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0011_alter_employee_id_restaurant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='id_restaurant',
        ),
    ]
