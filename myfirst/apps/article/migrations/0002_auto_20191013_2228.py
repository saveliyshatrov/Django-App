# Generated by Django 2.2.5 on 2019-10-13 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='article',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author_name',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment_text',
        ),
    ]
