from rest_framework import serializers

from food.models import Food
from food.models import Category


class FoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"


class CatSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"