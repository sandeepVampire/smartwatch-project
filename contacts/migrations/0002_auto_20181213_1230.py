# Generated by Django 2.1.1 on 2018-12-13 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='address',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='email_id',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='home',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='phone',
        ),
    ]
