#!/usr/bin/python3
"""A script to demonstrate the usage of the BaseModel class.

The script creates instance of BaseModel class, sets some attributes, saves the
object, converts it to a dictionary, and prints its JSON representation.

Usage:
    Execute this script to see an example of working with the BaseModel class.
"""
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json
                                   [key]))
