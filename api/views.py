from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class Home(APIView):
    def get(self, request):
        message = "Hello, First Pythonanywhere project!"
        return Response(message, status=status.HTTP_200_OK)