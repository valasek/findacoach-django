# Generated by Django 5.1 on 2024-09-01 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0002_alter_profile_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coachingsession',
            name='client',
        ),
        migrations.RemoveField(
            model_name='coachingsession',
            name='coach',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='CoachingSession',
        ),
    ]
