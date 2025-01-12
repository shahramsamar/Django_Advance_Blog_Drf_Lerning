
from django.urls import path, include
from accounts.api.v1 import views


app_name = 'api-v1'

urlpatterns = [
    # registration
    path('registration/', views.RegistrationApiView.as_view(),name='registrations'),
    # change password
    # reset password
    # login token
    # login jwt token

]
