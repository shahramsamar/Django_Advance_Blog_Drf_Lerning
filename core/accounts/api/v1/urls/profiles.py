from django.urls import path
from accounts.api.v1 import views




urlpatterns = [
    # profile
    path('',views.ProfileApiView.as_view(),name='Profile'),
    
]
