# Generated by Django 5.0.6 on 2024-05-27 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmodel',
            name='is_avaiable',
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]