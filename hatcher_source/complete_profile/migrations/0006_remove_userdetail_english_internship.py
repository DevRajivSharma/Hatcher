# Generated by Django 5.1.2 on 2025-02-02 13:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complete_profile', '0005_userdetail_english_level'),
        ('credentials', '0013_remove_user_table_age_remove_user_table_phone_no_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='english',
        ),
        migrations.CreateModel(
            name='internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('job_title', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='internships', to='credentials.user_table')),
            ],
        ),
    ]
