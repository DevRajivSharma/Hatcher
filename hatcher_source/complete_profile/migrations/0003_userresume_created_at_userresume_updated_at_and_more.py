# Generated by Django 5.1.2 on 2025-01-26 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complete_profile', '0002_userdetail_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='userresume',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='userresume',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='work_experience',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
