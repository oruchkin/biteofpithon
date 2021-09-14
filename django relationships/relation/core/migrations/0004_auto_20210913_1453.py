# Generated by Django 3.1.2 on 2021-09-13 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210913_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_rel', to='core.department'),
        ),
    ]
