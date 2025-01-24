# Generated by Django 5.1.2 on 2025-01-24 12:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complete_profile', '0003_alter_userdetail_salary'),
        ('credentials', '0013_remove_user_table_age_remove_user_table_phone_no_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='userResume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_file', models.FileField(upload_to='resume/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='resume', to='credentials.user_table')),
            ],
        ),
    ]
