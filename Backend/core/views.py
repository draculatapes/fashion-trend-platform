from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .models import Trend
from .serializers import TrendSerializer


@api_view(["GET"])
def trend_list(request):
    region_slug = request.GET.get("region")

    trends = Trend.objects.all().order_by("-created_at")

    if region_slug:
        trends = trends.filter(region__slug=region_slug)

    serializer = TrendSerializer(trends, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_trend(request):
    api_key = request.headers.get("X-ADMIN-KEY")

    if api_key != settings.ADMIN_API_KEY:
        return Response(
            {"error": "Unauthorized"},
            status=status.HTTP_401_UNAUTHORIZED
        )

    serializer = TrendSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)