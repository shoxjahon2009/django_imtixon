from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Food
from .models import Category
from django.contrib.sites import requests
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
#
from permissions import IsOwnUser
from serializers import FoodSerializers


class CreateFood(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [IsAuthenticated]


class RetriveUpdateFood(generics.RetrieveUpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers


class UpdateFood(generics.UpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [IsOwnUser]


class ListFood(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers


class DeleteFood(generics.DestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [IsAdminUser]


class CreateCat(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [IsAuthenticated]


class RetriveUpdateCat(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = FoodSerializers


class UpdateCat(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [IsOwnUser]


class DeleteCat(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [IsAdminUser]