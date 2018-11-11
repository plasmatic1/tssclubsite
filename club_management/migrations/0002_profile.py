# Generated by Django 2.1.3 on 2018-11-11 01:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, unique=True, validators=[django.core.validators.RegexValidator('^[a-z0-9]+$', 'Username must consist only characters and numbers.')])),
            ],
            options={
                'verbose_name': 'user profile',
                'db_table': 'user_profile',
            },
        ),
    ]