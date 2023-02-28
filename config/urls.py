from django.contrib import admin
from django.urls import path, include
from api.api import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]


