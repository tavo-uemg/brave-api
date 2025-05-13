from typing import Optional
from pydantic import BaseModel, Field

class Software(BaseModel):
    """A model representing a software entity."""

    name: Optional[str] = Field(
        default=None,
        description="The name of the software product."
    )
    author: Optional[str] = Field(
        default=None,
        description="The author of software product."
    )
    version: Optional[str] = Field(
        default=None,
        description="The latest version of the software product."
    )
    codeRepository: Optional[str] = Field(
        default=None,
        description="The code repository where the software product is currently available or maintained."
    )
    homepage: Optional[str] = Field(
        default=None,
        description="The home page of the software product."
    )
    datePublisher: Optional[str] = Field(
        default=None,
        description="The date when the software product was published."
    )
    is_npm: Optional[bool] = Field(
        default=False,
        description="Whether the software product is available on npm."
    )
    is_pypi: Optional[bool] = Field(
        default=False,
        description="Whether the software product is available on pypi."
    )
    stars: Optional[int] = Field(
        default=0,
        description="The number of stars on the repository."
    )
    forks: Optional[int] = Field(
        default=0,
        description="The numbers of forks of the repository."
    )
    ProgrammingLanguage: Optional[str] = Field(
        default=None,
        description="The programming language spread on the software product."
    )
