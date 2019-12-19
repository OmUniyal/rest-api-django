from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response


# Added after creating serializer file in profiles_api application
from rest_framework import status
from profiles_api import serializers

#imported for viewsets
from rest_framework import viewsets

#imported for UserProfileViewSet
from profiles_api import models

#imported for adding permissions to UserProfileViewSet
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions

#imported to add search filter
from rest_framework import filters

#imported to create login api viewset
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

#imported for permissions to Feed API
from rest_framework.permissions import IsAuthenticated

#APIView class
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
    

    #add serializer_class variable and write a post method to print "hello <name>"
    serializer_class = serializers.HelloSerializer

    def post(self, request):
        '''
        create hello message with the name input
        '''

        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        '''
        Handle updating an object
        '''
        return Response({'method':'PUT'})
    
    def patch(self, request, pk = None):
        '''
        Handle a partial update of an object.
        Only update fields that are provided in the request
        '''
        return Response({'method':'PATCH'})
    
    def delete(self, request, pk=None):
        '''
        Delete an object
        '''
        return Response({'method':'DELETE'})

#viewsets class
class HelloViewSets(viewsets.ViewSet):
    '''
    Test API viewset
    '''

    def list(self, request):
        '''
        Return a hello message
        '''
        a_viewset = [
            'uses actions (list, create, retrieve, update, partial_update, destroy)',
            'automatically maps to URLs using routers',
            'provides more functionality with less code',

        ]

        return Response({'message':'Hello!', 'a_viewset':a_viewset})

    def create(self, request):

        '''
        create a new hello message
        '''

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'

            return Response({'message': message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        '''
        Handle getting an object by its id
        '''
        return Response({'http_method','GET'})

    def update(self, request, pk=None):
        '''
        Handle updating an object
        '''
        return Response({'http_method':'PUT'})
    
    def partial_update(self, request, pk=None):
        '''
        Handle updating part of an object
        '''
        return Response({'http_method':'PATCH'})
    
    def destroy(self, request, pk=None):
        '''
        Handle deleting an object
        '''
        return Response({'http_method':'DELETE'})



#Creating user profile viewset

class UserProfileViewSet(viewsets.ModelViewSet):
    '''
    Handle creating and updating profiles
    '''

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    #adding permissions to this ViewSet
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    
    #Code for adding search filter
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

#UserLogin class

class UserLoginApiView(ObtainAuthToken):
    '''
    Handle creating user authentication tokens
    '''
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

#Viewset for Profile Feed
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    '''
    Handles creating, reading & updating profile feed items
    '''
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    
    #added while giving permissions to feed
    permission_classes = (permissions.UpdateOnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        '''
        sets the user profile to the logged in user
        '''
        serializer.save(user_profile = self.request.user)