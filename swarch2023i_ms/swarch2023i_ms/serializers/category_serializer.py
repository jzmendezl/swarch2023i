from rest_framework import serializers
from swarch2023i_ms.models.category_model import Category

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
