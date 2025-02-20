# Generated by Django 5.1.6 on 2025-02-17 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='netlify_movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(blank=True, max_length=50, null=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.EmailField(max_length=254, unique=True)),
                ('year_released', models.CharField(blank=True, max_length=50, null=True)),
                ('director', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
