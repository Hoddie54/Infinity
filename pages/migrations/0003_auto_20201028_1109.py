# Generated by Django 3.1.2 on 2020-10-28 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20201028_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='link',
            field=models.URLField(default='#'),
        ),
    ]
