# Generated by Django 4.0.3 on 2022-12-05 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_rename_blog_s_jobs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_s',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='blogs_image')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Jobs',
        ),
    ]