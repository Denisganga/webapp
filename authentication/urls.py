from django.urls import path
from .views import (Register,Login)

app_name= 'authentication'

urlpatterns = [
    # Add your URL patterns here
    path('register/', Register, name='register'),
    path('login/', Login, name='login')
]
