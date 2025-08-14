from django.urls import path
from .views import snake_view

urlpatterns = [
    path('', snake_view, name='snake'),
]

