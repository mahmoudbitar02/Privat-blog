# Generated by Django 4.2 on 2024-01-05 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_remove_education_last_remove_experience_last'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ('-year',)},
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'ordering': ('-year',)},
        ),
    ]
