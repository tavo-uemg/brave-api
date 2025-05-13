from pydantic import BaseModel, Field

from ..shared.thumbnail import Thumbnail
from .rating import Rating


class CreativeWork(BaseModel):
    """A creative work relevant to the query. An example can be enriched metadata for an app."""

    name: str = Field(description="The name of the creative work.")
    thumbnail: Thumbnail = Field(description="A thumbnail associated with the creative work.")
    rating: Rating = Field(default=None, description="A rating that is given to the creative work.")
