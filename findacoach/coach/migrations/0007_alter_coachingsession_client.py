# Generated by Django 5.1 on 2024-09-04 06:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0006_remove_client_session_coachingsession_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coachingsession',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coach.client', verbose_name='Client'),
        ),
    ]
