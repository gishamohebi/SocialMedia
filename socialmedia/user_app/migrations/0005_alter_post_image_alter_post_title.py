# Generated by Django 4.0.1 on 2022-01-11 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0004_post_date_alter_userinfo_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='post', max_length=50),
        ),
    ]
