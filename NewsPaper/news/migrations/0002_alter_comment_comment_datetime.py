# Generated by Django 4.1.5 on 2023-01-19 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]