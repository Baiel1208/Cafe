# Generated by Django 5.0 on 2024-01-01 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutStatic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('context', models.CharField(max_length=255, verbose_name='Описание')),
                ('number', models.CharField(max_length=100, verbose_name='Статистика')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'О нас и наши статистики',
            },
        ),
        migrations.RemoveField(
            model_name='settings',
            name='logo',
        ),
        migrations.AddField(
            model_name='settings',
            name='logo1',
            field=models.ImageField(blank=True, null=True, upload_to='settings', verbose_name='Логотип'),
        ),
        migrations.AddField(
            model_name='settings',
            name='logo2',
            field=models.ImageField(blank=True, null=True, upload_to='settings', verbose_name='Логотип-2'),
        ),
    ]