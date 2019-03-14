# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8-80 compliant>

bl_info = {
    "name" : "Surface Constraint Tools",
    "description" : (
        "A collection of tools for modeling on the surface of another mesh"
    ),
    "location" : "3D View > Tool Shelf > Surface Constraint Tools",
    "author" : "Brett Fedack",
    "version" : (1, 0),
    "blender" : (2, 76, 9),
    "category" : "3D View"
}

if "bpy" in locals():
    import importlib
    importlib.reload(MeshBrushProps)
    importlib.reload(ShrinkwrapProps)
    importlib.reload(SmoothVerticesProps)
    importlib.reload(SurfaceConstraintProps)
    importlib.reload(MeshBrush)
    importlib.reload(PickSurfaceConstraint)
    importlib.reload(Shrinkwrap)
    importlib.reload(SmoothVertices)
    importlib.reload(ResizeMeshBrush)
    importlib.reload(StrokeMove)
    importlib.reload(StrokeSmooth)
    importlib.reload(SurfaceConstraintToolsPanel)
    importlib.reload(SurfaceConstraintToolsPrefs)
else:
    from .properties import MeshBrushProps
    from .properties import ShrinkwrapProps
    from .properties import SmoothVerticesProps
    from .properties import SurfaceConstraintProps
    from .operators import MeshBrush
    from .operators import PickSurfaceConstraint
    from .operators import Shrinkwrap
    from .operators import SmoothVertices
    from .operators.internal import ResizeMeshBrush
    from .operators.internal import StrokeMove
    from .operators.internal import StrokeSmooth
    from .ui.panels import SurfaceConstraintToolsPanel
    from .preferences import SurfaceConstraintToolsPrefs

import bpy

import traceback

def register():
    try:
        bpy.utils.register_module(__name__)
    except: traceback.print_exc()

def unregister():
    try:
        bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()