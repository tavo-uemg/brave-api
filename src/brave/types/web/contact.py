from pydantic import BaseModel
from pydantic import Field
from .person import Thing

from typing import Optional


class Contact(BaseModel):
    """A model representing contact information for an entity."""

    email: Optional[str] = Field(default=None, description="The email address.")
    telephone: Optional[str] = Field(default=None, description="The telephone number.")

class ContactPoint(Thing):
    """A way to contact an entity."""
    type: str = Field(default="contact_point", description="A type string identifying a contact point. The value is always contact_point.")
    telephone: Optional[str] = Field(default=None, description="The telephone number of the entity.")
    email: Optional[str] = Field(default=None, description="The email address of the entity.")
