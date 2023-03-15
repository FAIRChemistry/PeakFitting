import sdRDM

from typing import List, Optional
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .parameter import Parameter
from .author import Author


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
        dataverse="pyDaRUS.Citation.description.text",
    )

    title: Optional[str] = Field(
        default=None,
        description="Title of the work",
        dataverse="pyDaRUS.Citation.title",
    )

    subject: List[str] = Field(
        description="Subject of matter linked to the dataset",
        default_factory=ListPlus,
        multiple=True,
        dataverse="pyDaRUS.Citation.subject",
    )

    authors: List[Author] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Authors of this dataset.",
    )

    parameters: List[Parameter] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Parameters to start and configure some process",
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

    def add_parameter_to_parameters(
        self,
        key: Optional[str] = None,
        value: Optional[float] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Parameter' to attribute parameters

        Args:
            id (str): Unique identifier of the 'Parameter' object. Defaults to 'None'.
            key (): Name of the parameter. Defaults to None
            value (): Respective value of a parameter. Defaults to None
        """

        params = {
            "key": key,
            "value": value,
        }

        if id is not None:
            params["id"] = id

        self.parameters.append(Parameter(**params))
