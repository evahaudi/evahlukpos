# Generated by Django 5.0.1 on 2024-01-31 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_users_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='name',
        ),
        migrations.AddField(
            model_name='users',
            name='fullname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='department',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
