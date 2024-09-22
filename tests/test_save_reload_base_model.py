#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

# Check all objects currently in storage
all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id, obj in all_objs.items():
    print(obj)

# Create a new object, set attributes, and save it
print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)

# Reload to verify persistence
print("-- Reloaded objects after saving --")
all_objs = storage.all()
for obj_id, obj in all_objs.items():
    print(obj)
