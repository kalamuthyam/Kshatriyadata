from  rest_framework.serializers import ModelSerializer
from  rest_framework import serializers
from .models import *

class SubscribersSerializer(ModelSerializer):
    class Meta:
        model = Subscribers
        fields ='__all__'

class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"