# Generated by Django 5.0.4 on 2024-05-04 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_menu_id_menu_remove_employee_vote_result_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='id_restaurant',
        ),
    ]
