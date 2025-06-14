from typing import Union
from typing import List
from typing import Optional

from pydantic import Field

from ..shared.custom_url import AutoHttpUrl
from ..shared.meta_url import MetaUrl
from ..shared.thumbnail import Thumbnail
from .data_provider import DataProvider
from .faq import QAPage
from .location_result import LocationResult
from .movie_data import MovieData
from .profile import Profile
from .rating import Rating
from .result import Result
from .unit import Unit


class AbstractGraphInfobox(Result):
    """Shared aggregated information on an entity from a knowledge graph."""

    type: str = Field(default="infobox", description="The infobox result type identifier.")
    position: int = Field(description="The position on a search result page.")
    label: str = Field(description="Label of the entity.")
    category: str = Field(description="Category of the entity.")
    long_desc: str = Field(description="Long description of the entity.")
    thumbnail: Thumbnail = Field(description="The thumbnail associated with the entity.")
    attributes: List[List[str]] = Field(description="A list of attributes about the entity.")
    profiles: Union[List[Profile], List[DataProvider]] = Field(description="The profiles associated with the entity.")
    website_url: AutoHttpUrl = Field(description="The official website pertaining to the entity.")
    ratings: List[Rating] = Field(description="Any ratings given to the entity.")
    providers: List[DataProvider] = Field(description="A list of data sources for the entity.")
    distance: Unit = Field(description="A unit representing quantity relevant to the entity.")
    images: List[Thumbnail] = Field(description="A list of images relevant to the entity.")
    movie: Optional[MovieData] = Field(
        description="Only when the result is a movie, any movie data relevant to the entity."
    )

class GenericInfobox(AbstractGraphInfobox):
    """Generic infobox."""

    subtype: str = Field(default="generic", description="The subtype of the infobox.")
    found_in_urls: List[str] = Field(description="URLs where the entity is found.")


class QAInfobox (AbstractGraphInfobox):
    """A question answer infobox."""

    subtype: str = Field(default="code", description="The infobox subtype identifier. The value is always code.")
    data: QAPage = Field(description="The question and relevant answer.")
    meta_url: MetaUrl = Field(description="Detailed information on the page containing the question and relevant answer.")


class InfoboxPlace (AbstractGraphInfobox):
    """An infobox for a place, such as a business."""

    subtype: str = Field(default="place", description="The infobox subtype identifier. The value is always place.")
    location: LocationResult = Field(description="The location result.")


class InfoboxWithLocation(AbstractGraphInfobox):
    """An infobox with location."""

    subtype: str = Field(default="location", description="The infobox subtype identifier. The value is always location.")
    is_location: bool = Field(description="Whether the entity is a location.")
    coordinates: List[float] = Field(description="The coordinates of the location.")
    zoom_level: int = Field(description="The map zoom level.")
    location: LocationResult = Field(description="The location result.")


class EntityInfobox(AbstractGraphInfobox):
    """An infobox for an entity."""

    subtype: str = Field(default="entity", description="The infobox subtype identifier. The value is always entity.")


class GraphInfobox(Result):
    """Aggregated information on an entity from a knowledge graph."""

    type: str = Field(default="graph", description="The type identifier for infoboxes. The value is always graph.")
    results: List[GenericInfobox | QAInfobox | InfoboxPlace | InfoboxWithLocation | EntityInfobox] = Field(description="A list of infoboxes associated with the query.")


class QAInfobox(GraphInfobox):
    """QA infobox."""

    subtype: str = Field(default="code", description="The subtype of the infobox.")
    data: QAPage = Field(description="QA page data.")
    meta_url: MetaUrl = Field(description="Aggregated information about the URL.")


class InfoboxWithLocation(AbstractGraphInfobox):
    """Infobox with location information."""

    subtype: str = Field(default="location", description="The subtype of the infobox.")
    is_location: bool = Field(description="Whether the entity is a location.")
    coordinates: List[float] = Field(description="[latitude, longitude]")
    zoom_level: int = Field(description="Zoom level for maps.")
    location: LocationResult = Field(description="Location result data.")


class InfoboxPlace(InfoboxWithLocation):
    """Place-specific infobox."""

    subtype: str = Field(default="place", description="The subtype of the infobox.")
    # Inherits all fields from InfoboxWithLocation and GenericInfobox
