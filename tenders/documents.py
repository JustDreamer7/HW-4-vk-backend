from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from users.models import User
from .models import Tenders


# from users.models import User


@registry.register_document
class TendersDocument(Document):
    class Index:
        name = 'tender'

    user = fields.ObjectField(
        properties={
            'email': fields.TextField(),
        })
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }

    class Django:
        model = Tenders

        fields = [
            'id',
            'title',
            'law',
            'price',
            'application_deadline',
        ]

        related_models = [User]

    def get_queryset(self):
        return super().get_queryset().select_related(
            'user'
        )

    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, User):
            return related_instance.tenders_set.all()
