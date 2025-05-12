from rest_framework import serializers
from .models import Item

# 1
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id','name','created']