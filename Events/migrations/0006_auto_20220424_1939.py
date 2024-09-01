# Generated by Django 3.2.3 on 2022-04-24 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0005_auto_20220424_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ourteam',
            name='sponsorstype',
        ),
        migrations.AddField(
            model_name='ourteam',
            name='post',
            field=models.CharField(choices=[('Dignitaries', 'Dignitaries'), ('Organizing Committee', 'Organizing Committee'), ('Core Committee', 'Core Committee')], default=1, max_length=30),
        ),
        migrations.AddField(
            model_name='ourteam',
            name='title',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
