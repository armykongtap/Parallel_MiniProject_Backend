# Generated by Django 3.0.3 on 2020-04-14 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_users',
            field=models.ManyToManyField(related_name='users_in_group', to='user.User'),
        ),
    ]