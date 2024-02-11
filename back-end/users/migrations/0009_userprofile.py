# Generated by Django 5.0.1 on 2024-02-04 21:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_rename_experience_years_users_experienceyears'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.ImageField(default='default_user_image.jpg', upload_to='user_images/')),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('experienceyears', models.IntegerField(blank=True, null=True)),
                ('department', models.CharField(blank=True, max_length=255, null=True)),
                ('fullname', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
