# Generated by Django 4.2.6 on 2023-10-14 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event',
            new_name='Events',
        ),
    ]