# Generated by Django 5.0.4 on 2024-05-04 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_alter_menu_id_restaurant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='id_menu',
        ),
    ]
