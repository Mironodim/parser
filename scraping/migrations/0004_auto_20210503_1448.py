# Generated by Django 3.1.5 on 2021-05-03 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0003_remove_job_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['my_time'], 'verbose_name': 'Игры', 'verbose_name_plural': 'Игры'},
        ),
    ]
