from django.http import HttpResponse
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

def update_model(request):
    objects = Test_model.objects.all()

    for obj in objects:
        obj.name = f"{obj.name} ({obj.id})"
        obj.save()
    return render(request,'update.html')

def delete_filter_model(request):
    objects = Test_model.objects.all()
    for obj in objects:
        if obj.id % 2 != 0:
            obj.delete()
    return render(request,'delete.html')