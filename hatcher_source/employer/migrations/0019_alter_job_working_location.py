# Generated by Django 5.1.2 on 2025-01-12 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0018_alter_job_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='working_location',
            field=models.CharField(choices=[('Work from home', 'Work from home'), ('Work from office', 'Work from office'), ('Field Job', 'Work from home and office')], max_length=100, null=True),
        ),
    ]
