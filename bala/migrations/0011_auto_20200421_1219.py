# Generated by Django 2.2.12 on 2020-04-21 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bala', '0010_projectmembers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='outcomes',
            old_name='Worker',
            new_name='worker',
        ),
    ]
