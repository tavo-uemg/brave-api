from typing import List

from pydantic import BaseModel, Field
from pydantic import HttpUrl

from ..shared.thumbnail import Thumbnail
from ..shared.meta_url import MetaUrl
from .contact import Contact
from .data_provider import DataProvider
from .opening_hours import OpeningHours
from .picture_results import PictureResults
from .postal_address import PostalAddress
from .rating import Rating
from .result import Result
from .reviews import Reviews
from .unit import Unit


class Action(BaseModel):
    """A model representing an action to be taken."""

    type: str = Field(description="The type representing the action.")
    url: HttpUrl = Field(description="A url representing the action to be taken.")


class LocationWebResult(Result):
    """A model representing a web result related to a location."""
    meta_url: MetaUrl = Field(description="Aggregated information about the url.")


class LocationResult(Result):
    """A result that is location relevant."""

    type: str = Field(
        default="location_result", description="Location result type identifier. The value is always location_result."
    )
    provider_url: HttpUrl = Field(description="The complete URL of the provider.")
    coordinates: List[float] = Field(
        description="A list of coordinates associated with the location. This is a lat long represented as a floating point."
    )
    zoom_level: int = Field(description="The zoom level on the map.")
    thumbnail: Thumbnail = Field(description="The thumbnail associated with the location.")
    postal_address: PostalAddress = Field(description="The postal address associated with the location.")
    opening_hours: OpeningHours = Field(
        description="The opening hours, if it is a business, associated with the location."
    )
    contact: Contact = Field(description="The contact of the business associated with the location.")
    price_range: str = Field(description="A display string used to show the price classification for the business.")
    rating: Rating = Field(description="The ratings of the business.")
    distance: Unit = Field(description="Distance to the location.")
    profiles: List[DataProvider] = Field(description="The associated profiles with the business.")
    reviews: Reviews = Field(description="Aggregated reviews from various sources relevant to the business.")
    pictures: PictureResults = Field(description="A bunch of pictures associated with the business.")
    action: Action = Field(description="An action to be taken.")
    serves_cuisine: List[str] = Field(description="A list of cuisine categories served.")
    categories: List[str] = Field(description="A list of categories.")
    icon_category: str = Field(description="An icon category.")
    results: LocationWebResult = Field(description="Web results related to this location.")
    timezone: str = Field(description="IANA timezone identifier.")
    timezone_offset: str = Field(description="The utc offset of the timezone.")


class Locations(LocationResult):
    """A model representing location results."""

    type: str = Field(default="locations", description="Location type identifier. The value is always locations.")
    results: List[LocationResult] = Field(description="An aggregated list of location sensitive results.")
