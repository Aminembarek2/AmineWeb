# Generated by Django 3.2.5 on 2021-07-14 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmineApp', '0003_alter_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='Astro', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
