# Generated by Django 3.2.5 on 2021-07-14 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmineApp', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='static/media/images/'),
        ),
    ]
