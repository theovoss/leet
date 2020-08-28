from rest_framework import serializers


class TwoSumSerializer(serializers.Serializer):
    numbers = serializers.JSONField(initial=[0, 2, 4, 77, 420], style={'base_template': 'input.html', 'input_type': 'text'})
    target = serializers.IntegerField(initial=81)
