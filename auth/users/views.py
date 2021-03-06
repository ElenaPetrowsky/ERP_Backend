from django.shortcuts import render
from rest_framework.views import APIView

from users import serializers
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class RegisterView(APIView):

    permission_classes=[IsAuthenticated]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
