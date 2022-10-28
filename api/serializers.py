from dataclasses import field
import imp
from rest_framework import serializers
from .models import MyDetails

class MyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyDetails
        fields = "__all__"