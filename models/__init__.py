#!/usr/bin/python3
"""__init__ magic method for models directory"""
from models.engine.file_storage import FileStorage

#creating a unique filestorage instance for my application
storage = FileStorage()

#calling the reload method on the storage instance
storage.reload()
