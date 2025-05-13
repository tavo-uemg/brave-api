from typing import Optional
from pydantic import BaseModel, Field
from ..shared.thumbnail import Thumbnail
from .rating import Rating

class MusicRecording(BaseModel):
    """Result classified as a music label or a song."""
    name: str = Field(
        description="The name of the music label or song or album.",
    )
    thumbnail: Optional[Thumbnail] = Field(
        default=None,
        description="A thumbnail associated with the music."
    )
    rating: Optional[Rating] = Field(
        default=None,
        description="The rating of the music."
    )