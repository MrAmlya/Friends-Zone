# Generated by Django 2.1.5 on 2020-05-25 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='hotel_Main_Img',
            field=models.ImageField(upload_to='media/images/'),
        ),
    ]
