# Generated by Django 5.0.6 on 2024-06-28 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giveaid', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unregistereddonation',
            old_name='firstname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='unregistereddonation',
            name='lastname',
        ),
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
