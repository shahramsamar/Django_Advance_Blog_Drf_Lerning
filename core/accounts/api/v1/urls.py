from django.urls import path, include
from accounts.api.v1.views import RegistrationApiView,CustomObtainAuthToken,CustomDiscardAuthToken
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


app_name = 'api-v1'

urlpatterns = [
    # registration
    path('registration/', RegistrationApiView.as_view(),name='registrations'),
    # login token
    path('token/login/',CustomObtainAuthToken.as_view(),name='token-login'),
    # logout token
    path('token/logout/',CustomDiscardAuthToken.as_view(),name='token-logout'),
    
    # change password
    
    # reset password
    
    # create jwt token
   path('jwt/create/', TokenObtainPairView.as_view(), name='jwt_create') ,
   # refresh jwt token
   path('api/token/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
   # verify jwt token
   path('api/token/verify/', TokenVerifyView.as_view(), name='jwt_verify'),
   
]
