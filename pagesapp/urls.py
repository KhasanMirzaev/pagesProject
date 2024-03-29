from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('services', ServicesPageView.as_view(), name='services'),
    path('info', InfoPageView.as_view(), name='info'),
]