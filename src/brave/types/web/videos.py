from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from ..shared.meta_url import MetaUrl
from ..shared.thumbnail import Thumbnail
from .profile import Profile
from .result import Result


class VideoData(BaseModel):
    """A model representing metadata gathered for a video."""

    duration: Optional[str] = Field(default=None, description="A time string representing the duration of the video.")
    views: Optional[int] = Field(default=None, description="The number of views of the video.")
    creator: Optional[str] = Field(default=None, description="The creator of the video.")
    publisher: Optional[str] = Field(default=None, description="The publisher of the video.")
    thumbnail: Optional[Thumbnail] = Field(default=None, description="A thumbnail associated with the video.")
    tags: List[str] = Field(default_factory=list, description="A list of tags associated with the video.")
    author: Optional[Profile] = Field(default=None, description="Author of the video.")
    requires_subscription: bool = Field(default=False, description="Whether the video requires a subscription to watch.")



class VideoResult(Result):
    """A model representing a video result."""

    type: str = Field(
        default="video_result", description="The type identifying the video result. The value is always video_result."
    )
    video: VideoData = Field(description="Metadata for the video.")
    meta_url: Optional[MetaUrl] = Field(default=None, description="Aggregated information on the URL.")
    thumbnail: Optional[Thumbnail] = Field(default=None, description="The thumbnail of the video.")
    age: Optional[str] = Field(default=None, description="A string representing the age of the video.")


class Videos(BaseModel):
    """A model representing video results."""

    type: str = Field(default="videos", description="The type representing the videos. The value is always videos.")
    results: List[VideoResult] = Field(description="A list of video results.")
    mutated_by_goggles: bool = Field(description="Whether the videos result were changed by a goggle.")
