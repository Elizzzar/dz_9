from django.urls import path
from .views import add_data

urlpatterns = [
    path('', add_data, name='add_data'),
]