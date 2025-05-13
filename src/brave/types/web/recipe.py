from typing import Optional, List
from pydantic import BaseModel, Field

from .videos import VideoData
from ..shared.thumbnail import Thumbnail
from .rating import Rating

class HowTo(BaseModel):
    """
    Aggregated information on how to do something.
    
    url: https://api.search.brave.com/app/documentation/web-search/responses#HowTo
    """

    text: str = Field(description="The how to text.")
    name: Optional[str] = Field(default=None, description="A name of the how to.")
    url: Optional[str] = Field(default=None, description="A URL associated with the how to.")
    image: Optional[List[str]] = Field(default=None, description="A list of images urls associated with the how to.")

class Recipe(BaseModel):
    """
    Aggregated information on a recipe.
    
    url: https://api.search.brave.com/app/documentation/web-search/responses#Recipe
    """

    title: str = Field(description="The title of the recipe.")
    description: str = Field(description="The description of the recipe.")
    thumbnail: Thumbnail = Field(description="A thumbnail associated with the recipe.")
    url: str = Field(description="The url of the web page where the recipe was found.")
    domain: str = Field(description="The domain of the web page where the recipe was found.")
    favicon: str = Field(description="The url for the favicon of the web page where the recipe was found.")
    time: Optional[str] = Field(default=None, description="The total time required to cook the recipe.")
    prep_time: Optional[str] = Field(default=None, description="The preparation time for the recipe.")
    cook_time: Optional[str] = Field(default=None, description="The cooking time for the recipe.")
    ingredients: Optional[str] = Field(default=None, description="Ingredients required for the recipe.")
    instructions: Optional[List[HowTo]] = Field(default=None, description="List of instructions for the recipe.")
    servings: Optional[int] = Field(default=None, description="How many people the recipe serves.")
    calories: Optional[int] = Field(default=None, description="Calorie count for the recipe.")
    rating: Optional[Rating] = Field(default=None, description="Aggregated information on the ratings associated with the recipe.")
    recipeCategory: Optional[str] = Field(default=None, description="The category of the recipe.")
    recipeCuisine: Optional[str] = Field(default=None, description="The cuisine classification for the recipe.")
    video: Optional[VideoData] = Field(default=None, description="Aggregated information on the cooking video associated with the recipe.")
