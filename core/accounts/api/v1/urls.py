from django.urls import path, include
from accounts.api.v1.views import RegistrationApiView,CustomObtainAuthToken
# from rest_framework.authtoken.views import ObtainAuthToken

app_name = 'api-v1'

urlpatterns = [
    # registration
    path('registration/', RegistrationApiView.as_view(),name='registrations'),
    path('token/login/',CustomObtainAuthToken.as_view(),name='token-login'),
    # change password
    # reset password
    # login token
    # login jwt token

]
