# Generated by Django 3.2 on 2023-01-29 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend',
            old_name='creator',
            new_name='user',
        ),
    ]
