from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from .serializers import Top10PollutedCitiesSerializer

class Top10PollutedCitiesView(APIView):
    def get(self, request):
        pass


class Top10CleanestCitiesView(APIView):
    def get(self, request):
        pass