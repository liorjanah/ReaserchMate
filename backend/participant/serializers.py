from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Participant


class ParticipantSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        try:
            participant = Participant.create(email=validated_data['email'],
                                             username=validated_data['username'],
                                             password=validated_data['password'],
                                             first_name=validated_data['first_name'],
                                             last_name=validated_data['last_name'],
                                             phone_number=validated_data['phone_number'])

            return participant

        except ValidationError as e:
            error = {'message': str(e) if len(e.args) > 0 else 'Unknown Error'}
            raise serializers.ValidationError(error)
