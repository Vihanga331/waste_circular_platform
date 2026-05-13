from rest_framework import serializers


class FutureEndpointSerializer(serializers.Serializer):
    name = serializers.CharField()
    status = serializers.CharField()
    owner = serializers.CharField()
