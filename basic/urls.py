from django.urls import path, include
from .views import *

urlpatterns = [
    path('items/', ItemDetail.as_view()),
]
