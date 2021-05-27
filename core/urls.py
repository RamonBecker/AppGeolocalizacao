from django.urls import path
from .views import IndexView

urlspatterns = [
    path('', IndexView.as_view(), name='index'),
]