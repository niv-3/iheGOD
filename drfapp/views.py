import joblib
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GenrePredictionSerializer

# Load the pre-trained model
model = joblib.load('Niv-music.pkl')

class GenrePrediction(APIView):
    def post(self, request):
        # Validate and serialize input data
        serializer = GenrePredictionSerializer(data=request.data)
        if serializer.is_valid():
            age = serializer.validated_data['age']
            gender = serializer.validated_data['gender']
            
            # Make prediction
            prediction = model.predict([[age, gender]])

            return Response({'predicted_genre': prediction[0]}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
