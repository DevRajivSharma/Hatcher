# Generated by Django 5.1.2 on 2025-01-11 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0013_alter_employer_table_phone_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='bio',
            new_name='desctiption',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='employees',
            new_name='total_staff',
        ),
    ]
