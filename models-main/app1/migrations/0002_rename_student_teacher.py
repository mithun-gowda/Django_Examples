# Generated by Django 4.1.5 on 2023-01-05 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='student',
            new_name='teacher',
        ),
    ]
