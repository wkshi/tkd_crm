from django.urls import path
from crm.views import *


urlpatterns = [
    path('', Index.as_view(), name='index'),
]