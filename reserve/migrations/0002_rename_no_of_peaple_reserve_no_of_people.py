# Generated by Django 4.2.4 on 2023-08-23 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserve',
            old_name='no_of_peaple',
            new_name='no_of_people',
        ),
    ]
