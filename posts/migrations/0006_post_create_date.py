# Generated by Django 4.2 on 2024-01-05 16:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_cattegory_post_cattegory'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='create_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
