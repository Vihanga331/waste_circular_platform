from rest_framework import serializers
from .models import WasteCategory, WasteCollection


class WasteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteCategory
        fields = "__all__"


class WasteCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteCollection
        fields = "__all__"
