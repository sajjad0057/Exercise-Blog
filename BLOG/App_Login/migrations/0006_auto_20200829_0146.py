# Generated by Django 3.1 on 2020-08-28 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0005_auto_20200829_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default='profile_pics/profile_pic.png', upload_to='profile_pics'),
        ),
    ]