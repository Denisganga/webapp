
from .views import (MainPage,Shop)
from django .urls import path


app_name='home_page'

urlpatterns=[
    path('mainpage/', MainPage, name='mainpage'),
    path('shop/', Shop, name='shop'),
]