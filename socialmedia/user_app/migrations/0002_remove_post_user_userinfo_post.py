# Generated by Django 4.0.1 on 2022-01-11 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='user_app.post'),
        ),
    ]