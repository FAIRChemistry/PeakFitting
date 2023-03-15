import sdRDM

from typing import List, Optional
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .ymatrix import YMatrix
from .units import Units


@forge_signature
class ExperimentalData(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("experimentaldataINDEX"),
        xml="@id",
    )

    x_values: List[float] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="x values of the experimental data e.g. time or angle.",
    )

    x_unit: Optional[Units] = Field(
        default=None,
        description="unit of the x values e.g. mm or degree.",
    )

    y_matrix: List[YMatrix] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="array of y values of corresponding x values.",
    )

    def add_y_matrix_to_y_matrix(
        self,
        y_values: List[float] = ListPlus(),
        y_unit: Optional[Units] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'YMatrix' to attribute y_matrix

        Args:
            id (str): Unique identifier of the 'YMatrix' object. Defaults to 'None'.
            y_values (): y values of the experimental data e.g. concentration or intensity.. Defaults to ListPlus()
            y_unit (): unit of the y values e.g. mol per l or arbitrary units. Defaults to None
        """

        params = {
            "y_values": y_values,
            "y_unit": y_unit,
        }

        if id is not None:
            params["id"] = id

        self.y_matrix.append(YMatrix(**params))
