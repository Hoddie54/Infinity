# Generated by Django 3.1.2 on 2020-10-29 23:07

import accounts.helper
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20201028_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='', validators=[accounts.helper.file_size]),
        ),
    ]
