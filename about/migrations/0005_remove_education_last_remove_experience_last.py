# Generated by Django 4.2 on 2024-01-05 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_alter_experience_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='last',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='last',
        ),
    ]
