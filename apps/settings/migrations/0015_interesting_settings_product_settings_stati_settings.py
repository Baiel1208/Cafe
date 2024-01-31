# Generated by Django 5.0 on 2024-01-10 20:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0014_interesting'),
    ]

    operations = [
        migrations.AddField(
            model_name='interesting',
            name='settings',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='interesting', to='settings.settings'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='settings',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='settings.settings'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stati',
            name='settings',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='stati', to='settings.settings'),
            preserve_default=False,
        ),
    ]