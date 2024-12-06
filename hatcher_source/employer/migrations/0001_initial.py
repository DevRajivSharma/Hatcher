# Generated by Django 5.1.2 on 2024-11-21 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employer_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('age', models.CharField(max_length=10, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.CharField(max_length=1000)),
                ('address', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='company_images')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('hr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.employer_table')),
            ],
        ),
    ]
