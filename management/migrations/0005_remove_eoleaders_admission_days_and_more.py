# Generated by Django 4.1.2 on 2024-02-22 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_directors_admission_days_employees_admission_days_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eoleaders',
            name='admission_days',
        ),
        migrations.RemoveField(
            model_name='otmleaders',
            name='admission_days',
        ),
        migrations.RemoveField(
            model_name='peleaders',
            name='admission_days',
        ),
    ]
