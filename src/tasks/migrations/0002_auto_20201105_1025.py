# Generated by Django 3.1 on 2020-11-05 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Taks',
            new_name='Task',
        ),
    ]