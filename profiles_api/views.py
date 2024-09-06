from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions

class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer
    def get(self,request,format = None):
        """Returns a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as function (get,post,patch,put,delete)',
        'Is similar to a traditonal Djano view',
        'Is mapped manually to Urls'
        ]

        return Response({'message': 'Success', 'an_apiview': an_apiview})

    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST)

class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        a_viewset = [
        'Uses actions (list, create, retrive, update, partial_uodate)',
        'Automatically maps to URLs using routers',
        'Provides more functionality with lessc code'
        ]
        return Response({'message': 'Hello', 'viewset': a_viewset})

    def create(self, request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name} !'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST)

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
