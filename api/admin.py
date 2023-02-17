from django.contrib import admin
from api.models import Book, RentBook, LibUser
# Register your models here.

admin.site.register(Book)
admin.site.register(RentBook)
admin.site.register(LibUser)
