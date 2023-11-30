# Generated by Django 4.2.4 on 2023-08-21 08:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0003_remove_profile_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='media')),
                ('checked', models.BooleanField(default=False)),
                ('slug', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.profile')),
            ],
        ),
    ]