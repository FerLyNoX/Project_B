# Generated by Django 2.2.12 on 2020-04-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bala', '0002_auto_20200414_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, default='', help_text='Заметки, чтобы не забыть', verbose_name='Описание'),
        ),
    ]
