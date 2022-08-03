# Copyright (c) 2022, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.
#
__all__ = ["ScatterWindow"]

import omni.ui as ui
from .style import scatter_window_style
from .utils import get_selection
from .combo_box_model import ComboBoxModel
from .scatter import scatter
from .utils import duplicate_prims


LABEL_WIDTH = 120
SPACING = 4


class ScatterWindow(ui.Window):
    """The class that represents the window"""

    def __init__(self, title: str, delegate=None, **kwargs):
        self.__label_width = LABEL_WIDTH

        super().__init__(title, **kwargs)

        # Models
        self._source_prim_model = ui.SimpleStringModel()
        self._scatter_prim_model = ui.SimpleStringModel()
        self._scatter_type_model = ComboBoxModel("Reference", "Copy", "PointInstancer")
        self._scatter_seed_model = ui.SimpleIntModel()
        self._scatter_count_models = [ui.SimpleIntModel(), ui.SimpleIntModel(), ui.SimpleIntModel()]
        self._scatter_distance_models = [ui.SimpleFloatModel(), ui.SimpleFloatModel(), ui.SimpleFloatModel()]
        self._scatter_random_models = [ui.SimpleFloatModel(), ui.SimpleFloatModel(), ui.SimpleFloatModel()]
        self._scale_models = [ui.SimpleFloatModel(), ui.SimpleFloatModel(), ui.SimpleFloatModel()]

        # Defaults
        self._scatter_prim_model.as_string = "/World/Scatter01"
        self._scatter_count_models[0].as_int = 15
        self._scatter_count_models[1].as_int = 1
        self._scatter_count_models[2].as_int = 1
        self._scatter_distance_models[0].as_float = 10
        self._scatter_distance_models[1].as_float = 10
        self._scatter_distance_models[2].as_float = 10
        self._scale_models[0].as_float = 1
        self._scale_models[1].as_float = 1
        self._scale_models[2].as_float = 1

        # Apply the style to all the widgets of this window
        self.frame.style = scatter_window_style
        # Set the function that is called to build widgets when the window is
        # visible
        self.frame.set_build_fn(self._build_fn)

    def destroy(self):
        # It will destroy all the children
        super().destroy()

    @property
    def label_width(self):
        """The width of the attribute label"""
        return self.__label_width

    @label_width.setter
    def label_width(self, value):
        """The width of the attribute label"""
        self.__label_width = value
        self.frame.rebuild()

    def _on_get_selection(self):
        """Called when tthe user presses the "Get From Selection" button"""
        self._source_prim_model.as_string = ", ".join(get_selection())

    def _on_scatter(self):
        """Called when the user presses the "Scatter" button"""
        prim_names = [i.strip() for i in self._source_prim_model.as_string.split(",")]
        if not prim_names:
            prim_names = get_selection()

        if not prim_names:
            # TODO: "Can't clone" message
            pass

        transforms = scatter(
            count=[m.as_int for m in self._scatter_count_models],
            distance=[m.as_float for m in self._scatter_distance_models],
            randomization=[m.as_float for m in self._scatter_random_models],
            id_count=len(prim_names),
            seed=self._scatter_seed_model.as_int,
        )

        duplicate_prims(
            transforms=transforms,
            prim_names=prim_names,
            target_path=self._scatter_prim_model.as_string,
            mode=self._scatter_type_model.get_current_item().as_string
        )

    def _build_source(self):
        """Build the widgets of the "Source" group"""
        with ui.CollapsableFrame("Source", name="group"):
            with ui.VStack(height=0, spacing=SPACING):
                with ui.HStack():
                    ui.Label("Prim", name="attribute_name", width=self.label_width)
                    ui.StringField(model=self._source_prim_model)
                    # Button that puts the selection to the string field
                    ui.Button(
                        " S ",
                        width=0,
                        height=0,
                        style={"margin": 0},
                        clicked_fn=self._on_get_selection,
                        tooltip="Get From Selection",
                    )

    def _build_scatter(self):
        """Build the widgets of the "Scatter" group"""
        with ui.CollapsableFrame("Scatter", name="group"):
            with ui.VStack(height=0, spacing=SPACING):
                with ui.HStack():
                    ui.Label("Prim Path", name="attribute_name", width=self.label_width)
                    ui.StringField(model=self._scatter_prim_model)

                with ui.HStack():
                    ui.Label("Prim Type", name="attribute_name", width=self.label_width)
                    ui.ComboBox(self._scatter_type_model)

                with ui.HStack():
                    ui.Label("Seed", name="attribute_name", width=self.label_width)
                    ui.IntDrag(model=self._scatter_seed_model, min=0, max=10000)

                with ui.HStack():
                    ui.Label("Scale", name="attribute_name", width=self.label_width)
                    for field in zip(["X:", "Y:", "Z:"], self._scale_models):
                        ui.Label(field[0], width=0, style={"margin": 3.0})
                        ui.FloatField(model=field[1], height=0, style={"margin": 3.0})



    def _build_axis(self, axis_id, axis_name):
        """Build the widgets of the "X" or "Y" or "Z" group"""
        with ui.CollapsableFrame(axis_name, name="group"):
            with ui.VStack(height=0, spacing=SPACING):
                with ui.HStack():
                    ui.Label("Object Count", name="attribute_name", width=self.label_width)
                    ui.IntDrag(model=self._scatter_count_models[axis_id], min=1, max=100)

                with ui.HStack():
                    ui.Label("Distance", name="attribute_name", width=self.label_width)
                    ui.FloatDrag(self._scatter_distance_models[axis_id], min=0, max=10000)

                with ui.HStack():
                    ui.Label("Random", name="attribute_name", width=self.label_width)
                    ui.FloatDrag(self._scatter_random_models[axis_id], min=0, max=10000)

    def _build_fn(self):
        """
        The method that is called to build all the UI once the window is
        visible.
        """
        with ui.ScrollingFrame():
            with ui.VStack(height=0):
                self._build_source()
                self._build_scatter()
                self._build_axis(0, "X Axis")
                self._build_axis(1, "Y Axis")
                self._build_axis(2, "Z Axis")

                # The Go button
                ui.Button("Scatter", clicked_fn=self._on_scatter)
