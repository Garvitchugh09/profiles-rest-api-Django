from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API view"""
    def get(self,request,format = None):
        """Returns a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as function (get,post,patch,put,delete)',
        'Is similar to a traditonal Djano view',
        'Is mapped manually to Urls'
        ]

        return Response({'message': 'Success', 'an_apiview': an_apiview})
