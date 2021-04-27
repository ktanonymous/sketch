from django.shortcuts import render
from rest_framwork import status
from rest_framework.view import APIView
from rest_framework.response import Response

from .models import Users
from ..friend.models import Friends

# Create your views here.
