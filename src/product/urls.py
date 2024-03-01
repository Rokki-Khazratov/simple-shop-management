from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('minus/', minus, name='minus'),
    path('come/', come, name='minus'),
    path('deptor', deptor, name='deptor'),
    path('trade/', trade, name='trade'),
]
