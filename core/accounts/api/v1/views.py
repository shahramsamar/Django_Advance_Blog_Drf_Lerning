from rest_framework import generics 
from rest_framework.response  import Response
from .serializers import RegistrationSerializer
from  rest_framework import status




class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data ={
                'email': serializer.validated_data['email']
            }
            # return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(data,status=status.HTTP_201_CREATED)
        # The line `return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)` is
        # returning a response with the validation errors from the serializer in case the data
        # provided in the request is not valid.
        # This line of code is returning a response with the validation errors from the serializer in
        # case the data provided in the request is not valid. The `serializer.errors` contains a
        # dictionary of field-level errors that occurred during validation. By returning this response
        # with a status of `HTTP_400_BAD_REQUEST`, it indicates that the request data was not valid
        # and provides the client with information about the specific validation errors that occurred.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    