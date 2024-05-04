# Generated by Django 5.0.4 on 2024-05-04 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='id_menu',
            field=models.IntegerField(null=True),
        ),
        migrations.RemoveField(
            model_name='employee',
            name='vote_result',
        ),
        migrations.AddField(
            model_name='employee',
            name='vote_result',
            field=models.ManyToManyField(related_name='employees_voted', to='restaurant.menu'),
        ),
    ]