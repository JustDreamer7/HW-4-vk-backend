from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

from .serializers import User, ElasticUserSerializer

@receiver(pre_save, sender=User, dispatch_uid="update_record")
def update_es_record(sender, instance, **kwargs):
    obj = ElasticUserSerializer(instance)
    obj.save()


@receiver(post_delete, sender=User, dispatch_uid="delete_record")
def delete_es_record(sender, instance, *args, **kwargs):
    obj = ElasticUserSerializer(instance)
    obj.delete(ignore=404)
