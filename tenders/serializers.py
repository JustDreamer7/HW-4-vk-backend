from rest_framework import serializers
from rest_framework_elasticsearch.es_serializer import ElasticModelSerializer
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from tenders.documents import TendersDocument
from tenders.models import Tenders
from users.models import User


class TenderSerializer(serializers.ModelSerializer):
    user = serializers.EmailField()

    class Meta:
        model = Tenders
        fields = ['id', 'title', 'law', 'price', 'application_deadline', 'user']

    # def validate(self, data):
    #     for key in ('title'):
    #         if 'tender' in data[key].lower():
    #             raise serializers.ValidationError(f'{key} field contains tender, I dont like it')
    #     return data

    def create(self, validated_data):
        test = validated_data.get("user", None)
        validated_data.pop("user")
        return Tenders.objects.create(user=User.objects.get(email=test), **validated_data)

    def update(self, instance, validated_data):
        test = validated_data.get("user", None)
        validated_data.pop("user")
        instance.title = validated_data['title']
        instance.law = validated_data['law']
        instance.price = validated_data['price']
        instance.application_deadline = validated_data['application_deadline']
        instance.user = User.objects.get(email=test)
        instance.save()
        return instance


class ElasticTenderSerializer(DocumentSerializer):
    class Meta:
        model = Tenders
        document = TendersDocument
        fields = ['id', 'title', 'law', 'price','application_deadline', 'user']
