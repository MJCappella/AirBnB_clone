#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city in the system."""

    def __init__(self, *args, **kwargs):
        """Initialize a new City."""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
