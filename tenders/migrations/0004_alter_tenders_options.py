# Generated by Django 3.2.9 on 2021-11-12 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0003_alter_tenders_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tenders',
            options={'verbose_name': 'Тендер', 'verbose_name_plural': 'Тендеры'},
        ),
    ]
