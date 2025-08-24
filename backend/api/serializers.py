from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","password"]
        extra_kwargs = {"password":{"write_only": True}}

    def create(self, validated_data):
        """Accepts validated_data from the Meta class above and use it to create a user. Data is validated by ModelSerializer"""
        user = User.objects.create_user(**validated_data) #create_user() automatically handles password hashing (unlike User.objects.create())
        return user