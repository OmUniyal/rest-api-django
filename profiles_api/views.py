from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    '''
    Test API View
    '''

    def get(self, request, format = None):
        '''
        Returns a list of API view features
        '''

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'is similar to traditional django view',
            'gives control over application\'s logic',
            'is mapped manually to URLs',
        ]

        return Response({'message':'Hello!', 'an_apiview': an_apiview})
