# Generated by Django 3.1.2 on 2020-11-03 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20201101_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoAddApplication',
            fields=[
                ('application_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.application')),
            ],
            bases=('pages.application',),
        ),
    ]
