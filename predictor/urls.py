# predictor/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Map the root URL of the app to the predict_personality view
    path('', views.predict_personality, name='predict_personality'),
]