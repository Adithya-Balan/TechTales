# Generated by Django 5.1.1 on 2024-09-18 03:49

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_blogs_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
