# Generated by Django 5.1.6 on 2025-02-17 14:47

import users.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_managers_user_is_active_user_is_staff'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.managers.UserManager()),
            ],
        ),
    ]
