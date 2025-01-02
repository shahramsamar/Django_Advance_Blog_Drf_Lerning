from  rest_framework import  generics
from rest_framework.response  import Response
from .serializers import RegistrationSerializer
from 



class RegistrationApiView(generics.GenericsAPIView):
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            
            data ={
                'email': serializer.validated_data['email']
            }
        return Response(data,status=)