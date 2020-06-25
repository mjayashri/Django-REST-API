from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Retrieve a list f API view features"""
        an_apiview = [
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'My first APIVIEW',
            'Information from the list present in APIVIEW'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        """create a hello message with our name"""
        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializers.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """Handle updating the objct"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handle partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})