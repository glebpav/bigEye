from rest_framework import serializers

from .models import *

class EmployeeSerializer(serializers.Serializer):
    fio = serializers.CharField(max_length=255)
    profession = serializers.CharField(max_length=255)
    email = serializers.EmailField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.fio = validated_data.get('fio', instance.fio)
        instance.profession = validated_data.get('profession', instance.profession)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class DataCollectionSerializer(serializers.Serializer):
    rating = serializers.CharField(max_length=255)
    time = serializers.CharField(max_length=255)
    employeeId = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return DataCollection.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.rating = validated_data.get('rating', instance.rating)
        instance.time = validated_data.get('time', instance.time)
        instance.employeeId = validated_data.get('employeeId', instance.employeeId)
        instance.save()
        return instance
