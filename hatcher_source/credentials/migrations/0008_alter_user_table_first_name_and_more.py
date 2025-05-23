# Generated by Django 5.1.2 on 2025-01-09 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0007_feedback_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_table',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user_table',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user_table',
            name='phone_no',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user_table',
            name='user_bio',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
