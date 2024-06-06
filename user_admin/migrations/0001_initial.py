# Generated by Django 5.0.6 on 2024-06-06 22:59

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAdminModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(default=True, max_length=150, unique=True)),
                ('password', models.CharField(default='default_value_here', max_length=150)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
    ]