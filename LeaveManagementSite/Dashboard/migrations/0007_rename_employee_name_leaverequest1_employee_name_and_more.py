# Generated by Django 5.1.7 on 2025-04-08 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0006_remove_leaverequest1_status_leaverequest1_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaverequest1',
            old_name='Employee_name',
            new_name='employee_name',
        ),
        migrations.RenameField(
            model_name='leaverequest1',
            old_name='End_date',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='leaverequest1',
            old_name='Leave_type',
            new_name='leave_type',
        ),
        migrations.RenameField(
            model_name='leaverequest1',
            old_name='Start_date',
            new_name='start_date',
        ),
    ]
