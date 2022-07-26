# Copyright (c) 2022, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.
#
__all__ = ["ScatterCreatePointInstancerCommand"]

from pxr import Gf
from pxr import Sdf
from pxr import Usd
from pxr import UsdGeom
from typing import List
from typing import Optional
from typing import Tuple
import omni.kit.commands
import omni.usd.commands


class ScatterCreatePointInstancerCommand(omni.kit.commands.Command, omni.usd.commands.stage_helper.UsdStageHelper):
    """
    Create PointInstancer undoable **Command**.

    ### Arguments:

        `path_to: str`
            The path for the new prims

        `transforms: List`
            Pairs containing transform matrices and ids to apply to new objects

        `prim_names: List[str]`
            Prims to duplicate
    """

    def __init__(
        self,
        path_to: str,
        transforms: List[Tuple[Gf.Matrix4d, int]],
        prim_names: List[str],
        stage: Optional[Usd.Stage] = None,
        context_name: Optional[str] = None,
    ):
        omni.usd.commands.stage_helper.UsdStageHelper.__init__(self, stage, context_name)
        self._path_to = path_to

        # We have it like [(tr, id), (tr, id), ...]
        # It will be transformaed to [[tr, tr, ...], [id, id, ...]]
        unzipped = list(zip(*transforms))

        self._positions = [m.ExtractTranslation() for m in unzipped[0]]
        self._proto_indices = unzipped[1]
        self._prim_names = prim_names.copy()

    def do(self):
        stage = self._get_stage()

        # Set up PointInstancer
        instancer = UsdGeom.PointInstancer.Define(stage, Sdf.Path(self._path_to))
        attr = instancer.CreatePrototypesRel()
        for name in self._prim_names:
            attr.AddTarget(Sdf.Path(name))
        instancer.CreatePositionsAttr().Set(self._positions)
        instancer.CreateProtoIndicesAttr().Set(self._proto_indices)

    def undo(self):
        delete_cmd = omni.usd.commands.DeletePrimsCommand([self._path_to])
        delete_cmd.do()
