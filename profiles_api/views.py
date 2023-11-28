from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

# Create your views here.
class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        an_apiview = [
            'this is the most common things',
            'hello i am ibadat hossain',
            'ki chai tor',
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk = None):
        return Response({'methods':'PUT'})

    def patch(self, request, pk =None):
        return Response({'methods':'PATCH'})

    def delete(self, request, pk = None):
        return Response({'methods':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer
    def list(self,request):
        a_viewset = [
            'haha what are you doing',
            'no this is not possible',
        ]
        return Response({'message':'Hello!', 'a_viewset' : a_viewset})

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        return Response({'http_method':'GET'})


    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        return Response({'http_method':'DELETE'})

