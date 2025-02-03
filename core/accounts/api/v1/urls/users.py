from django.urls import path
from accounts.api.v1.views import (RegistrationApiView,
                                   CustomObtainAuthToken,
                                   CustomDiscardAuthToken)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from accounts.api.v1 import views


urlpatterns = [
    # registration
    path('registration/', RegistrationApiView.as_view(),name='registrations'),
    # login token
    path('token/login/',CustomObtainAuthToken.as_view(),name='token-login'),
    # logout token
    path('token/logout/',CustomDiscardAuthToken.as_view(),name='token-logout'),
    # change password
    path('change-password/',views.ChangePasswordApiView.as_view(),name='change-password'),
   
    # activation
    path('activation/confirm/<str:token>',views.ActivationApiView.as_view(),name='Activation'),
    # resend activation
    path('activation/resend',views.ActivationResendApiView.as_view(),name='resend-activation'),

    # reset password

    # activation test
    # path('activation/confirm/',views.EmailSend.as_view(),name='change-password'),
    # create jwt token
    # path('jwt/create/', TokenObtainPairView.as_view(), name='jwt_create') , 
    # custom jwt token
    path('jwt/create/',views.CustomTokenObtainPairView.as_view(), name='jwt_create') ,
    # refresh jwt token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    # verify jwt token
    path('api/token/verify/', TokenVerifyView.as_view(), name='jwt_verify'),

]
