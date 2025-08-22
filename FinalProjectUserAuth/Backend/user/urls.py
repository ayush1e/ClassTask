
from django.urls import path 

from .views import  login, registration, dashboard

urlpatterns = [
    
    path('login/', login),
    path('registration/', registration),
    path('dashboard/', dashboard),
    
]