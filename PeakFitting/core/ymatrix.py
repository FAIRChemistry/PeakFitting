import sdRDM

from typing import List, Optional
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .units import Units


@forge_signature
class YMatrix(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("ymatrixINDEX"),
        xml="@id",
    )

    y_values: List[float] = Field(
        default_factory=ListPlus,
        multiple=True,
        description=(
            "y values of the experimental data e.g. concentration or intensity."
        ),
    )

    y_unit: Optional[Units] = Field(
        default=None,
        description="unit of the y values e.g. mol per l or arbitrary units",
    )
