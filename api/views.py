from django.shortcuts import render
from .models import City
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer

# Create your views here.
class CityView(APIView):
    
    class CitySerializer(ModelSerializer):
        
        class Meta:
            model = City
            fields = ('title',)
    
    def get(self, request, format=None):
        cities = City.objects.all()
        data = self.CitySerializer(cities, many=True).data
        return Response({'cities': data})


class SlackEventHookView(APIView):
    
    def post(self, request, format=None):
        print(request.data)
        return Response({'success': True})