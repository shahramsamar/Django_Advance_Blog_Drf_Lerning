
from django.urls import path, include
from blog.api.v1 import views


app_name = 'api-v1'

urlpatterns = [
    # registration
    path('registration/', views.RegistrationApiView.as_view(),'registrations'),
    # change password
    # reset password
    # login token
    # login jwt token

]
