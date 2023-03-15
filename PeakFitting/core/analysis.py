import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


from .metadata import Metadata
from .experimentaldata import ExperimentalData


@forge_signature
class Analysis(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("analysisINDEX"),
        xml="@id",
    )

    metadata: Optional[Metadata] = Field(
        default=None,
        description="metadata of the corresponding measuring data.",
    )

    experimental_data: Optional[ExperimentalData] = Field(
        default=None,
        description="experimental data of a measurement.",
    )
