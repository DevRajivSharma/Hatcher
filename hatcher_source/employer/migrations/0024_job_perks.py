# Generated by Django 5.1.2 on 2025-01-13 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0023_rename_working_location_job_work_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='perks',
            field=models.CharField(max_length=100, null=True),
        ),
    ]