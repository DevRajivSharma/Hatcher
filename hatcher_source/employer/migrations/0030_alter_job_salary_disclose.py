# Generated by Django 5.1.2 on 2025-01-15 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0029_job_salary_disclose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='salary_disclose',
            field=models.BooleanField(default=False),
        ),
    ]