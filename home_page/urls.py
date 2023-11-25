
from .views import (MainPage)
from django .urls import path


app_name='home_page'

urlpatterns=[
    path('mainpage/', MainPage, name='mainpage'),
]