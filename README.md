# AirBnB_clone
The first step towards building our first full web application is to write a command interpreter to manage our AirBnB objects. This step is crucial as we will use what we build during this project with all other following projects, including HTML/CSS templating, database storage, API, and front-end integration.

# Generally it involves tasks to:

1. Put in place a parent class (called BaseModel) to take care of the initialization, serialization, and deserialization of your future instances.
2. Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
3. Create all classes used for AirBnB (User, State, City, Place, etc.) that inherit from BaseModel.
4. Create the first abstracted storage engine of the project: File storage.
5. Create all unit tests to validate all your classes and the storage engine and the  rsource that could help with this is [The link](https://docs.python.org/3/library/unittest.html#module-unittest).
