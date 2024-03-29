# Generated by Django 3.1.2 on 2020-10-31 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20201030_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='stage',
            field=models.CharField(choices=[('Stage 1', 'Stage 1'), ('Stage 2', 'Stage2'), ('3', 'Stage 3'), ('4', 'Stage4'), ('5', 'Stage 5')], default='Stage 1', max_length=150),
        ),
        migrations.AlterField(
            model_name='notes',
            name='notes1',
            field=models.TextField(blank=True, default='', verbose_name='Stage 1'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='notes2',
            field=models.TextField(blank=True, default='', verbose_name='Stage2'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='notes3',
            field=models.TextField(blank=True, default='', verbose_name='Stage 3'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='notes4',
            field=models.TextField(blank=True, default='', verbose_name='Stage4'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='notes5',
            field=models.TextField(blank=True, default='', verbose_name='Stage 5'),
        ),
    ]
