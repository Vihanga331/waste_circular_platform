from rest_framework import serializers
from .models import GasCylinder, MethaneProduction


class MethaneProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MethaneProduction
        fields = "__all__"


class GasCylinderSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasCylinder
        fields = "__all__"
