# Generated by Django 5.0 on 2024-01-09 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0009_alter_about_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stati',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('context', models.CharField(max_length=255, verbose_name='Описание')),
                ('number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Статистика')),
            ],
        ),
        migrations.RemoveField(
            model_name='about',
            name='number',
        ),
    ]
