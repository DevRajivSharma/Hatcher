# Generated by Django 5.1.2 on 2025-01-26 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community_post', '0004_alter_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]