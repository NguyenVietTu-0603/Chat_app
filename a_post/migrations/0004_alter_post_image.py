# Generated by Django 5.1.6 on 2025-03-16 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_post', '0003_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post/'),
        ),
    ]
