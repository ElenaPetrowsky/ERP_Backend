import email
from unicodedata import name
from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        Model = User
        fields = "__all__"