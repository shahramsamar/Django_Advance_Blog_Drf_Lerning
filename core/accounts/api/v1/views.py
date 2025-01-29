from rest_framework import generics ,status
from rest_framework.response  import Response
from .serializers import RegistrationSerializer,CustomAuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


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
    
    
class CustomObtainAuthToken(ObtainAuthToken):
        serializer_class = CustomAuthTokenSerializer

        def post(self, request, *args, **kwargs):
            serializer = self.serializer_class(data=request.data,
                                            context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email
            })
            
class CustomDiscardAuthToken(APIView):            
    permission_classes = [IsAuthenticated]
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)