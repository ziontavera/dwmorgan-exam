# Generated by Django 4.2.1 on 2023-05-12 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CovidObservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observation_date', models.DateTimeField()),
                ('province', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('last_update', models.DateTimeField()),
                ('confirmed', models.IntegerField()),
                ('deaths', models.IntegerField()),
                ('recovered', models.IntegerField()),
            ],
        ),
    ]
