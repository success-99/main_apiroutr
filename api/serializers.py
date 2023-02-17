from rest_framework import serializers
from .models import Book, LibUser, RentBook


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class LibUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = LibUser
        fields = '__all__'


class RentBookSerializers(serializers.ModelSerializer):
    class Meta:
        model = RentBook
        fields = '__all__'
