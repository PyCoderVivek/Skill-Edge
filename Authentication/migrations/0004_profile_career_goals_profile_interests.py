# Generated by Django 5.1.4 on 2024-12-23 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0003_rename_field_of_study_profile_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='career_goals',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='interests',
            field=models.TextField(blank=True, null=True),
        ),
    ]