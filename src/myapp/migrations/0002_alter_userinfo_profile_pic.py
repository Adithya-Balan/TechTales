# Generated by Django 5.1.1 on 2024-09-17 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='profile_pic',
            field=models.ImageField(default='profile_pic/profile.jpg', upload_to='profile_pic'),
        ),
    ]
