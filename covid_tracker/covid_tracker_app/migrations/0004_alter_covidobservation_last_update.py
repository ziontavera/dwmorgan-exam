# Generated by Django 4.2.1 on 2023-05-12 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid_tracker_app', '0003_alter_covidobservation_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covidobservation',
            name='last_update',
            field=models.DateTimeField(),
        ),
    ]