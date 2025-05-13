from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from ..shared.thumbnail import Thumbnail


class Thing(BaseModel):
    """
    A model representing a generic thing.
    
    https://api-dashboard.search.brave.com/app/documentation/web-search/responses#Thing
    """

    type: str = Field(default="thing", description="A type identifying a thing. The value is always thing.")
    name: str = Field(description="The name of the thing.")
    url: Optional[str] = Field(default=None, description="A URL for the thing.")
    thumbnail: Optional[Thumbnail] = Field(default=None, description="Thumbnail associated with the thing.")


class Person(Thing):
    """A model representing a person entity"""

    type: Optional[str] = Field(
        default="person", description="A type identifying a person. The value is always person."
    )
