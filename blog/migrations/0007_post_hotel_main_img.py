# Generated by Django 2.2.12 on 2020-05-29 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200525_0729'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hotel_Main_Img',
            field=models.ImageField(default=0, upload_to='images/'),
            preserve_default=False,
        ),
    ]
