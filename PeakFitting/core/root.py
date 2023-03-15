import sdRDM

from typing import List, Optional
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .author import Author
from .analysis import Analysis


@forge_signature
class Root(sdRDM.DataModel):

    """This is the root of the data model and contains all objects defined in this example. While its good practice to have a single root, you can define as many roots as you like. Furthermore, the name does not have to be ```Root``` and can be any other name."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("rootINDEX"),
        xml="@id",
    )

    description: Optional[str] = Field(
        default=None,
        description="Describes the content of the dataset.",
    )

    title: Optional[str] = Field(
        default=None,
        description="Title of the work",
    )

    subject: List[str] = Field(
        description="Subject of matter linked to the dataset",
        default_factory=ListPlus,
        multiple=True,
    )

    authors: List[Author] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Authors of this dataset.",
    )

    analysis: Optional[Analysis] = Field(
        default=None,
        description="analysis part of this dataset.",
    )

    def add_author_to_authors(
        self,
        name: Optional[str] = None,
        affiliation: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Author' to attribute authors

        Args:
            id (str): Unique identifier of the 'Author' object. Defaults to 'None'.
            name (): Full name including given and family name. Defaults to None
            affiliation (): To which organization the author is affiliated to. Defaults to None
        """

        params = {
            "name": name,
            "affiliation": affiliation,
        }

        if id is not None:
            params["id"] = id

        self.authors.append(Author(**params))
