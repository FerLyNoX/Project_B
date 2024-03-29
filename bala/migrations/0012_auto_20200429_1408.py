# Generated by Django 2.2.12 on 2020-04-29 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bala', '0011_auto_20200421_1219'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incomes',
            options={'ordering': ('date',), 'verbose_name': 'Поступления', 'verbose_name_plural': 'Поступления'},
        ),
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ('name',), 'verbose_name': 'Работа', 'verbose_name_plural': 'Работы'},
        ),
        migrations.AlterModelOptions(
            name='outcomes',
            options={'ordering': ('date',), 'verbose_name': 'Расход', 'verbose_name_plural': 'Расходы'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('name',), 'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterModelOptions(
            name='worker',
            options={'ordering': ('name',), 'verbose_name': 'Работник', 'verbose_name_plural': 'Работники'},
        ),
        migrations.AddField(
            model_name='project',
            name='closed',
            field=models.BooleanField(blank=True, default=False, verbose_name='Проект закрыт'),
        ),
    ]
