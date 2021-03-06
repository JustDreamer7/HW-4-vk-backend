# Generated by Django 3.2.9 on 2021-11-15 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tenders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=64, verbose_name='Название тендера')),
                ('law', models.CharField(blank=True, choices=[('44-ФЗ', 'Main Law'), ('94-ФЗ', 'Add Law First'), ('223-ФЗ', 'Add Law Second')], default='44-ФЗ', max_length=10, verbose_name='Закон')),
                ('price', models.FloatField(null=True, verbose_name='Цена работ')),
                ('application_deadline', models.DateField(null=True, verbose_name='Срок подачи заявок')),
            ],
            options={
                'verbose_name': 'Тендер',
                'verbose_name_plural': 'Тендеры',
            },
        ),
    ]
