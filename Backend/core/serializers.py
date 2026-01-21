from rest_framework import serializers
from .models import Trend


class TrendSerializer(serializers.ModelSerializer):
    region = serializers.StringRelatedField()

    class Meta:
        model = Trend
        fields = ['id', 'title', 'region', 'category', 'status', 'created_at']
