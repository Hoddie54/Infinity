# Generated by Django 3.1.2 on 2020-11-04 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_auto_20201103_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='close_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='open_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
