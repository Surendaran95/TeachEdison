# Generated by Django 4.2.5 on 2023-09-23 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='bio',
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.CharField(default='', max_length=200),
        ),
    ]