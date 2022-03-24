# Generated by Django 4.0.1 on 2022-01-11 21:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Enter your first name', max_length=50)),
                ('last_name', models.CharField(help_text='Enter your last name', max_length=50, null=True)),
                ('phone_number', models.IntegerField(help_text='Your phone number', max_length=12, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('id_code', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(10)])),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('text', models.TextField(blank=True, help_text='caption', null=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.userinfo')),
            ],
        ),
    ]