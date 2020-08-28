from rest_framework import serializers


class TwoSumSerializer(serializers.Serializer):
    numbers = serializers.JSONField(default=[0, 2, 4, 77, 420])
    target = serializers.IntegerField(default=81)
