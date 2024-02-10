#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):

    """
    Represents an amenity in the system.
    """
    def __init__(self, *args, **kwargs):

        """Initialize a new Amenity."""

        super().__init__(*args, **kwargs)
        self.name = ""
