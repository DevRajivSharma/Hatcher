# Generated by Django 5.1.2 on 2024-12-01 08:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '__first__'),
        ('dashboard', '0006_user_table_alter_application_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credentials.user_table'),
        ),
        migrations.DeleteModel(
            name='user_table',
        ),
    ]
