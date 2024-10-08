# Generated by Django 4.0.4 on 2022-05-02 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0011_event_club_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='coordinator_name',
            new_name='coordinator_name_1',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='coordinator_no',
            new_name='coordinator_no_1',
        ),
        migrations.AddField(
            model_name='event',
            name='coordinator_name_2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='coordinator_no_2',
            field=models.CharField(default='', max_length=10),
        ),
    ]
