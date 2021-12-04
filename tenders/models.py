from django.db import models
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.urls import reverse

from tenders.tasks import admin_informer
from users.models import User


# Create your models here.
class Tenders(models.Model):
    class TenderLaw(models.TextChoices):
        main_law = '44-ФЗ'
        add_law_first = '94-ФЗ'
        add_law_second = '223-ФЗ'

    title = models.CharField(max_length=64, null=False, blank=True, verbose_name='Название тендера')
    law = models.CharField(max_length=10, null=False, blank=True, verbose_name='Закон', default=TenderLaw.main_law,
                           choices=TenderLaw.choices)
    price = models.FloatField(verbose_name='Цена работ', null=True)
    application_deadline = models.DateField(verbose_name='Срок подачи заявок', null=True)
    # tender_creator = models.ForeignKey(User, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tender', kwargs={'tender_id': self.id})

    class Meta:
        verbose_name = 'Тендер'
        verbose_name_plural = 'Тендеры'


@receiver(pre_save, sender=Tenders)
def send_info_mail(sender, **kwargs):
    admin_informer.delay()
