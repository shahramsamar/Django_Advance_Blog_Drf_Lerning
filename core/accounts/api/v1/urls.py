from django.urls import path, include
from accounts.api.v1.views import RegistrationApiView,CustomObtainAuthToken,CustomDiscardAuthToken
# from rest_framework.authtoken.views import ObtainAuthToken

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
    
    # login jwt token

]
