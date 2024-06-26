# Generated by Django 5.0.4 on 2024-05-03 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_restaurant', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('vote_result', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_restaurant', models.IntegerField()),
                ('name_restaurant', models.CharField(max_length=255)),
                ('menu_update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
