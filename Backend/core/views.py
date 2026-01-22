from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .models import Trend,Region
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
def create_region(request):
    api_key = request.headers.get("X-ADMIN-KEY")

    if api_key != settings.ADMIN_API_KEY:
        return Response({"error": "Unauthorized"}, status=401)

    name = request.data.get("name")
    slug = request.data.get("slug")

    region = Region.objects.create(name=name, slug=slug)
    return Response({"id": region.id, "name": region.name})