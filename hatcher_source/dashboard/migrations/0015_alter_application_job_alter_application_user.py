# Generated by Django 5.1.2 on 2025-01-28 11:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0013_remove_user_table_age_remove_user_table_phone_no_and_more'),
        ('dashboard', '0014_alter_application_status'),
        ('employer', '0033_job_current_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='employer.job'),
        ),
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='credentials.user_table'),
        ),
    ]
