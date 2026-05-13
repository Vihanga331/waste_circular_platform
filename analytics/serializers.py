from rest_framework import serializers
from .models import Notification, SustainabilityMetrics


class SustainabilityMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SustainabilityMetrics
        fields = "__all__"


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"
