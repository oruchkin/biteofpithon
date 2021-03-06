# Generated by Django 3.1.2 on 2021-01-18 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_auto_20210117_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passengers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flights.Flight')),
            ],
        ),
    ]
