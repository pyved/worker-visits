from rest_framework import serializers
from .models import Unit, Visit

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'name']


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'


class GetVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['id', "visit_created"]