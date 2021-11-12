from django.db import models

from users.models import Users


# Create your models here.
class Tenders(models.Model):
    class TenderLaw(models.TextChoices):
        main_law = '44-ФЗ'
        add_law_first = '94-ФЗ'
        add_law_second = '223-ФЗ'

    title = models.CharField(max_length=64, null=False, verbose_name='Название тендера')
    law = models.CharField(max_length=10, null=False, verbose_name='Закон', default=TenderLaw.main_law,
                           choices=TenderLaw.choices)
    price = models.FloatField(verbose_name='Цена работ', null=True)
    application_deadline = models.DateField(verbose_name='Срок подачи заявок', null=True)
    # tender_creator = models.ForeignKey(Users, to_field='username', on_delete=models.PROTECT)
    company = models.ForeignKey(Users, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Тендер'
        verbose_name_plural = 'Тендеры'