# Generated by Django 5.1.2 on 2024-12-25 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0008_alter_job_company_req_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(max_length=100, null=True),
        ),
    ]