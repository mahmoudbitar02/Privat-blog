# Generated by Django 4.2 on 2024-01-04 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_alter_about_cv_alter_education_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='year',
            field=models.IntegerField(),
        ),
    ]
