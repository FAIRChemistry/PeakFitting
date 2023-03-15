import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


from .xrd import XRD
from .nmr import NMR
from .gc import GC
from .ir import IR


@forge_signature
class Metadata(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("metadataINDEX"),
        xml="@id",
    )

    IR: Optional[IR] = Field(
        default=None,
        description="IR measurement.",
    )

    XRD: Optional[XRD] = Field(
        default=None,
        description="XRD measurement.",
    )

    GC: Optional[GC] = Field(
        default=None,
        description="GC measurement.",
    )

    NMR: Optional[NMR] = Field(
        default=None,
        description="NMR measurement.",
    )
