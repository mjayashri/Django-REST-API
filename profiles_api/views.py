from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API view"""
    def get(self,request,format=None):
        """Retrieve a list f API view features"""
        an_apiview = [
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'My first APIVIEW',
            'Information from the list present in APIVIEW'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

