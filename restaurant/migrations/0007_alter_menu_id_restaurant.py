# Generated by Django 5.0.4 on 2024-05-04 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_alter_employee_id_restaurant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='id_restaurant',
            field=models.IntegerField(null=True),
        ),
    ]
