# Generated by Django 4.2.4 on 2023-08-24 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0005_remove_reserve_time_reserve_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserve',
            name='time',
        ),
        migrations.AddField(
            model_name='reserve',
            name='time',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
