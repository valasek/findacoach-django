# Generated by Django 5.1 on 2024-09-01 21:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0004_coachingsession_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='hours_delivered',
            field=models.DecimalField(blank=True, decimal_places=1, help_text='Hours in 0.5 steps', max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999.5)], verbose_name='Hours delivered'),
        ),
        migrations.AlterField(
            model_name='client',
            name='hours_ordered',
            field=models.DecimalField(blank=True, decimal_places=1, help_text='Hours in 0.5 steps', max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999.5)], verbose_name='Hours ordered'),
        ),
    ]
