from rest_framework import serializers

from tenders.models import Tenders
from users.models import User


class TenderSerializer(serializers.ModelSerializer):
    user = serializers.EmailField()

    class Meta:
        model = Tenders
        fields = ['id', 'title', 'law', 'price', 'application_deadline', 'user']

    def validate(self, data):
        for key in ('title', 'body'):
            if 'tender' in data[key].lower():
                raise serializers.ValidationError(f'{key} field contains hello, I dont like it')

        return data

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
