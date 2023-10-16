from django.shortcuts import render
from .models import Test_model

def add_data(request):
    data_list = [
        {"name": "test1", "array_json": ["value1", "value2", "value3"]},
        {"name": "test2", "array_json": ["value4", "value5", "value6"]},
    ]
    for data in data_list:
        my_model_instance = Test_model(
            name=data['name'],  
            array_json=data['array_json'],
        )
        my_model_instance.save()
    
    return render(request,'base.html')