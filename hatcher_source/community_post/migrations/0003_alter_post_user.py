# Generated by Django 5.1.2 on 2024-12-07 07:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community_post', '0002_alter_post_user'),
        ('credentials', '0004_remove_user_table_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credentials.user_table'),
        ),
    ]
