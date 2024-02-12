#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review in the system."""

    def __init__(self, *args, **kwargs):
        """Initialize a new Review."""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
