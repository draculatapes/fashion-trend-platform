from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Trend
from .serializers import TrendSerializer


@api_view(['GET'])
def trend_list(request):
    region_slug = request.GET.get('region')

    trends = Trend.objects.all().order_by('-created_at')

    if region_slug:
        trends = trends.filter(region__slug=region_slug)

    serializer = TrendSerializer(trends, many=True)
    return Response(serializer.data)
