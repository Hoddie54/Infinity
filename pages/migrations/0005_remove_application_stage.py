# Generated by Django 3.1.2 on 2020-10-29 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20201029_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='stage',
        ),
    ]
