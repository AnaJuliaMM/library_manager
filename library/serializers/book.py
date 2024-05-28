from rest_framework import serializers
from ..models.book import BookModel

class BookSerializer(serializers.ModelSerializer):
    class Meta: 
        model = BookModel
        fields =  '__all__'