# Generated by Django 4.0.3 on 2022-12-05 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_job_delete_job_s'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Job',
            new_name='Blogs',
        ),
    ]