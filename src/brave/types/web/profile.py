from pydantic import BaseModel, Field, HttpUrl

from ..shared.custom_url import AutoHttpUrl


class Profile(BaseModel):
    """
    Profile of an entity.

    url: https://api.search.brave.com/app/documentation/web-search/responses#Profile
    """

    name: str = Field(description="The name of the profile.")
    long_name: str = Field(description="The long name of the profile.")
    url: AutoHttpUrl = Field(description="The original URL where the profile is available.")
    img: HttpUrl = Field(description="The served image URL representing the profile.")
