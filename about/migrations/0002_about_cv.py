# Generated by Django 4.2 on 2024-01-03 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='cv',
            field=models.FileField(default='', upload_to='cv'),
            preserve_default=False,
        ),
    ]
