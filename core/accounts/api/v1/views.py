from rest_framework import generics ,status
from rest_framework.response  import Response
from .serializers import (RegistrationSerializer,CustomAuthTokenSerializer,
                          CustomTokenObtainPairSerializer,ChangePasswordSerializer,
                          ProfileSerializer)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from accounts.models import User
from ...models import Profile
from django.shortcuts import get_object_or_404



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
 
    
class CustomTokenObtainPairView(TokenObtainPairView):
        serializer_class = CustomTokenObtainPairSerializer
 

class ChangePasswordApiView(generics.GenericAPIView):
   model = User
   permission_classes = [IsAuthenticated]
   serializer_class = ChangePasswordSerializer
   def get_object(self,queryset=None):
       obj = self.request.user
       return obj
   
   def put(self, request, *args, **kwargs):
       self.object = self.get_object()
       Serializer = self.get_serializer(data=request.data)
       if Serializer.is_valid():
            if not self.object.check_password(Serializer.data.get('old_password')):
                return Response({'old_password':['Warning password']},status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(Serializer.data.get('new_password'))
            self.object.save()
            return Response({'detail':'change password successfully'}, status=status.HTTP_200_OK)
       return Response(Serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   
class ProfileApiView(generics.RetrieveUpdateAPIView):
       serializer_class = ProfileSerializer
       queryset = Profile.objects.all()
       
       def get_object(self):
           queryset = self.get_queryset()
           obj = get_object_or_404(queryset, user=self.request.user) 
           return obj