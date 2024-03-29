# Generated by Django 5.0 on 2024-01-11 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0021_rename_name_contacts_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog', verbose_name='Фото')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('interesting_text', models.TextField(verbose_name='Интересный текст')),
                ('text', models.TextField(verbose_name='Текст')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовка')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Блог',
            },
        ),
        migrations.RenameModel(
            old_name='contacts',
            new_name='Сontacts',
        ),
    ]
