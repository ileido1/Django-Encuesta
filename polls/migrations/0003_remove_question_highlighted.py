# Generated by Django 3.0.4 on 2020-03-28 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200326_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='highlighted',
        ),
    ]
