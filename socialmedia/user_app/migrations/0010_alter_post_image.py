# Generated by Django 4.0.1 on 2022-02-02 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0009_rename_userinfo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, upload_to='media', verbose_name='Image'),
        ),
    ]