# Generated by Django 3.1.2 on 2020-11-02 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20201102_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='article',
            name='firm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article', to='articles.firm'),
        ),
    ]
