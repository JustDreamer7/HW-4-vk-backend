from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers

from users.documents import UserDocument
from users.models import User


# from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'company', 'is_superuser']

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        instance.email = validated_data['email']
        instance.company = validated_data['company']
        instance.is_superuser = validated_data['is_superuser']
        instance.save()
        return instance


class ElasticUserSerializer(DocumentSerializer):
    class Meta:
        model = User
        document = UserDocument
        fields = ['id', 'username', 'email', 'company', 'is_superuser']
