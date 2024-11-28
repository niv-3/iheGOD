from django.urls import path
from .views import GenrePrediction  # Correctly import from your app's views.py

urlpatterns = [
    path('', GenrePrediction.as_view(), name='genre_prediction'),  # Add the endpoint for the prediction
]
