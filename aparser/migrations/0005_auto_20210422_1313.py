# Generated by Django 3.1.6 on 2021-04-22 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparser', '0004_auto_20210422_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.TextField(default='password', verbose_name='Пароль'),
        ),
        migrations.AddField(
            model_name='users',
            name='username',
            field=models.TextField(default='user', verbose_name='Имя пользователя'),
        ),
    ]
