from typing import List

from pydantic import BaseModel
from pydantic import Field

from .button_result import ButtonResult
from .image import Image
from .news import NewsResult
from .videos import VideoResult


class DeepResult(BaseModel):
    """Aggregated deep results from news social videos and images."""

    news: List[NewsResult] = Field(default=[], description="A list of news results associated with the result.")
    buttons: List[ButtonResult] = Field(default=[], description="A list of buttoned results associated with the result.")
    videos: List[VideoResult] = Field(default=[], description="Videos associated with the result.")
    images: List[Image] = Field(default=[], description="Images associated with the result.")
