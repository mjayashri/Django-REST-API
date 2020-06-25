from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """serializes the name field for apiview"""
    name = serializers.CharField(max_length=10)
