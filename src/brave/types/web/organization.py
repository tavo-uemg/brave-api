from typing import List

from pydantic import Field

from .person import Thing
from .contact import ContactPoint


class Organization(Thing):
    """An entity responsible for another entity."""

    type: str = Field(
        default="organization",
        description="A type string identifying an organization. The value is always organization.",
    )
    contact_points: List[ContactPoint] = Field(
        default_factory=list,
        description="A list of contact points for the organization."
    )