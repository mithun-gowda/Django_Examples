# Generated by Django 4.1.5 on 2023-01-15 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PersonalDetails',
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
