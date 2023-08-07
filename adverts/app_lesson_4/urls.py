from django.urls import path
from .views import func1


urlpatterns = [
    path('', func1)
]