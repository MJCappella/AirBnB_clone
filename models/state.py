#!/usr/bin/python3
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state in the system."""

    def __init__(self, *args, **kwargs):
        """Initialize a new State."""
        super().__init__(*args, **kwargs)
        self.name = ""
