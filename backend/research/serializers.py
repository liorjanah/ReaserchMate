from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Research


class ResearchSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        try:
            research = Research.create(name=validated_data.get('name'), field_id=validated_data.get('field').id,
                                       capacity=validated_data.get('capacity'))
            return research

        except ValidationError as e:
            error = {'message': str(e) if len(e.args) > 0 else 'Unknown Error'}
            raise serializers.ValidationError(error)

    class Meta:
        model = Research
        fields = ('id', 'name', 'field', 'capacity')
