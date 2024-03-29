# Generated by Django 3.1.2 on 2020-10-30 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20201030_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='application',
        ),
        migrations.AddField(
            model_name='application',
            name='notes',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='pages.notes'),
        ),
        migrations.AlterField(
            model_name='application',
            name='stage',
            field=models.CharField(choices=[('1', 'Stage 1'), ('2', 'Stage2'), ('3', 'Stage 3'), ('4', 'Stage4'), ('5', 'Stage 5')], default='1', max_length=150),
        ),
        migrations.AlterField(
            model_name='notes',
            name='notes1',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='notes',
            name='notes2',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='notes',
            name='notes3',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='notes',
            name='notes4',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='notes',
            name='notes5',
            field=models.TextField(default=''),
        ),
    ]
