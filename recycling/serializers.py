from rest_framework import serializers
from .models import RecyclingInventory


class RecyclingInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecyclingInventory
        fields = "__all__"
