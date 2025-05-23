# Generated by Django 5.1.4 on 2024-12-24 22:47

import zaza_interior.web.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=20, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=15, validators=[zaza_interior.web.validators.validate_phone_number], verbose_name='Phone number')),
                ('message', models.TextField(verbose_name='Message')),
            ],
        ),
    ]
