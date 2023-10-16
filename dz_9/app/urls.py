from django.urls import path
from .views import *

urlpatterns = [
    path('', add_data, name='add_data'),
    path('/update', update_model, name='update_model'),
    path('/delete', delete_filter_model, name='delete_filter_model'),
]