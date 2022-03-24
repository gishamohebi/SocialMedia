# Generated by Django 4.0.1 on 2022-01-11 22:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0006_alter_post_image_alter_userinfo_phone_number_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='id_code',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(100)]),
        ),
    ]