from django.shortcuts import render
from rest_framework import viewsets
from api.models import Book, LibUser, RentBook
from api.serializers import BookSerializers, LibUserSerializers, RentBookSerializers


# Create your views here.

class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class LibUserViewSet(viewsets.ModelViewSet):
    queryset = LibUser.objects.all()
    serializer_class = LibUserSerializers


class RentBookViewSet(viewsets.ModelViewSet):
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializers
