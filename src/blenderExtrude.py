import bpy

bpy.context.scene.unit_settings.length_unit = 'MILLIMETERS'
bpy.context.scene.unit_settings.scale_length = 0.001

bpy.ops.import_curve.svg (filepath=bpy.path.abspath("//test_map.svg"))

bpy.ops.object.select_all(action='DESELECT')

baseHeight = 0.4 # thickness of the 3d printed base, recommend 2 layers or more
mapHeight = 7 # Overall map height

# These are extra and cause trouble
bpy.data.objects.remove(bpy.data.objects['Curve.001'], do_unlink=True)
bpy.data.objects.remove(bpy.data.objects['Curve.002'], do_unlink=True)

for obj in bpy.data.collections[1].all_objects:
    if obj.type == 'CURVE':
        if obj.data.materials[0]:
            obj.data.extrude = (baseHeight + ( mapHeight - baseHeight) * obj.data.materials[0].diffuse_color[0] ) / 2 # divide by two because this extrudes this amount up AND down
            obj.location[2] = obj.data.extrude * obj.scale[2] # Shift up to compensate for extrusion down
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)
        bpy.ops.object.convert(target='MESH')
        obj.select_set(False)
    # obj.scale[0] = 100
    # obj.scale[1] = 100
    # obj.scale[2] = 100

# I think blender just isn't the right tool for dealing with
# shrinking the map down to the right level and using booleans.
# It tends to leave a mess and a ton of open faces.

# Scale and position the default cube
#bpy.data.objects['Cube'].scale = [ 2.75, 2.75, 0.1 ]
#bpy.data.objects['Cube'].location = [ 2.75, 2.75, 0.1 ]
bpy.data.objects['Cube'].scale = [ 5, 5, 0.2 ]
bpy.data.objects['Cube'].location = [ 100, 110, 0.2 ]
#bpy.data.objects['Cube'].hide_viewport = True


# # And, for every object, set up an intersection with the cube.
# for obj in bpy.data.collections[1].all_objects:
#     obj.modifiers.new(type='BOOLEAN', name='CubeIntersect')
#     obj.modifiers["CubeIntersect"].operation = 'INTERSECT'
#     obj.modifiers["CubeIntersect"].object = bpy.data.objects['Cube']
#     #obj.modifier_apply(apply_as='DATA', modifier="CubeIntersect")
#     obj.select_set(True)
#     bpy.ops.object.modifier_apply(apply_as='DATA', modifier='CubeIntersect')
#     obj.select_set(False)
# And delete the cube
# bpy.data.objects.remove(bpy.data.objects['Cube'], do_unlink=True)

# Set selection for exporting (so we don't get the bounding cube)
#bpy.ops.object.select_all(action='DESELECT')
#for obj in bpy.data.collections[1].all_objects:
#    obj.select_set(True)

#bpy.ops.export_mesh.stl(filepath=bpy.path.abspath("//test_map.stl"), use_selection=True, check_existing=False)

bpy.ops.export_mesh.stl(filepath=bpy.path.abspath("//test_map.stl"), check_existing=False)
