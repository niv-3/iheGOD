from rest_framework import serializers

class GenrePredictionSerializer(serializers.Serializer):
    age = serializers.IntegerField()
    gender = serializers.IntegerField()

    def validate_gender(self, value):
        if value not in [0, 1]:
            raise serializers.ValidationError("Gender must be 0 (female) or 1 (male).")
        return value
