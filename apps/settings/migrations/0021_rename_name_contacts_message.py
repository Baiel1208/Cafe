# Generated by Django 5.0 on 2024-01-11 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0020_contacts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='name',
            new_name='message',
        ),
    ]