# Generated by Django 5.1.6 on 2025-02-18 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netlify_movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Netflix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(blank=True, max_length=50, unique=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=128)),
                ('year_released', models.CharField(blank=True, max_length=50, null=True)),
                ('director', models.CharField(blank=True, max_length=50, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
            ],
            options={
                'verbose_name_plural': 'Netflix',
            },
        ),
    ]
