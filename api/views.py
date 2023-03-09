from django.shortcuts import render
from django.conf import settings
from .models import City
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer
import slack


client = slack.WebClient(token=settings.BOT_USER_ACCESS_TOKEN)

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


class SlackSendView(APIView):
    
    def post(self, request, format=None):
        data = request.data
        client.chat_postMessage(channel='#test', text=data['text'])
        return Response({'success': True})

class SlackEventHookView(APIView):
    
    def post(self, request, format=None):
        print(request.data)
        return Response({'success': True})