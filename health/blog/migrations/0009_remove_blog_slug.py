# Generated by Django 3.0.6 on 2020-05-28 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blog_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='slug',
        ),
    ]
