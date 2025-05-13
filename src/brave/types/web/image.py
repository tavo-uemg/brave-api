from pydantic import BaseModel
from pydantic import Field

from ..shared.custom_url import AutoHttpUrl
from ..shared.thumbnail import Thumbnail


class ImageProperties(BaseModel):
    """Metadata on an image."""

    url: AutoHttpUrl = Field(description="The image URL.")
    resized: AutoHttpUrl = Field(description="The resized image.")
    placeholder: AutoHttpUrl = Field(description="The placeholder image.")
    height: int = Field(description="The height of the image.")
    width: int = Field(description="The width of the image.")
    format: str = Field(description="The format specifier for the image.")
    content_size: str = Field(description="The image storage size.")


class Image(BaseModel):
    """A model describing an image."""

    thumbnail: Thumbnail = Field(description="The thumbnail associated with the image.")
    url: AutoHttpUrl = Field(description="The URL of the image.")
    properties: ImageProperties = Field(description="Metadata on the image.")
