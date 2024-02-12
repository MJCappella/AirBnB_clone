#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user in the system."""

    def __init__(self, *args, **kwargs):
        """Initialize a new User."""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
