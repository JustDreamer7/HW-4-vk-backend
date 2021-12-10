from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

from .serializers import Tenders, ElasticTenderSerializer


@receiver(pre_save, sender=Tenders, dispatch_uid="update_record")
def update_es_record(sender, instance, **kwargs):
    obj = ElasticTenderSerializer(instance)
    obj.save()


@receiver(post_delete, sender=Tenders, dispatch_uid="delete_record")
def delete_es_record(sender, instance, *args, **kwargs):
    obj = ElasticTenderSerializer(instance)
    obj.delete(ignore=404)
