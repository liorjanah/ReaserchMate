from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Participant


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')


class ParticipantSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    def create(self, validated_data):
        try:
            participant = Participant.create(email=validated_data['user']['email'],
                                             username=validated_data['user']['username'],
                                             password=validated_data['user']['password'],
                                             first_name=validated_data['first_name'],
                                             last_name=validated_data['last_name'],
                                             phone_number=validated_data['phone_number'])

            return participant

        except ValidationError as e:
            error = {'message': str(e) if len(e.args) > 0 else 'Unknown Error'}
            raise serializers.ValidationError(error)

    class Meta:
        model = Participant
        fields = ('id', 'user', 'first_name', 'last_name', 'phone_number')
        depth = 1
