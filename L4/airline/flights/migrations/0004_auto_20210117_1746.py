# Generated by Django 3.1.2 on 2021-01-17 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_auto_20210117_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='code',
            field=models.CharField(max_length=3),
        ),
    ]
