# Generated by Django 5.1.2 on 2024-11-21 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='translation',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
