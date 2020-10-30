from rest_framework import serializers
from activities.models import Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            'id',
            'title',
            'title',
            'address',
            'description',
            'created_at',
            'updated_at',
            'disabled_at',
            'status'
        ]
