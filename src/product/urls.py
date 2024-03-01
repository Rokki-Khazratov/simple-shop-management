from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),


    path('trade/', trade, name='trade'),
    path('debetors', debetors, name='debetors'),

    path('all_products/', all_products, name='all_products'),
    path('notifacation/', notifacation, name='notifacation'),
]
