# Generated by Django 5.1.2 on 2025-01-28 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0032_remove_job_timesince'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='current_application',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
