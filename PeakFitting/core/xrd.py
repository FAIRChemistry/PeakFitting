import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class XRD(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("xrdINDEX"),
        xml="@id",
    )

    placeholder: Optional[str] = Field(
        default=None,
        description="placeholder",
    )
