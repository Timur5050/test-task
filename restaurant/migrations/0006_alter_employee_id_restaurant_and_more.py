# Generated by Django 5.0.4 on 2024-05-04 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_remove_restaurant_id_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id_restaurant',
            field=models.IntegerField(null=True),
        ),
        migrations.RemoveField(
            model_name='employee',
            name='vote_result',
        ),
        migrations.AddField(
            model_name='employee',
            name='vote_result',
            field=models.IntegerField(null=True),
        ),
    ]