# Generated by Django 5.1.2 on 2025-01-12 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0020_job_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(blank=True, default='company_images/default', null=True, upload_to='company_images'),
        ),
    ]