from django.shortcuts import render
from rest_framwork import status
from rest_framework.view import APIView
from rest_framework.response import Response

from .models import User
from .models import Friend
from .models import Event

# Create your views here.
