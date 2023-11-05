# Generated by Django 4.2.6 on 2023-10-14 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'm'), ('female', 'f')], max_length=100)),
                ('interest', models.CharField(max_length=25)),
                ('country', models.CharField(choices=[('India', 'India'), ('foreign', 'foreign')], max_length=100)),
            ],
            options={
                'db_table': 'Attendee',
            },
        ),
        migrations.CreateModel(
            name='Organiser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('category', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'Organiser',
            },
        ),
    ]
