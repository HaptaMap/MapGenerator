import bpy

bpy.context.scene.unit_settings.length_unit = 'MILLIMETERS'

bpy.ops.import_curve.svg (filepath=bpy.path.abspath("//test_map.svg"))

bpy.ops.object.select_all(action='DESELECT')

for obj in bpy.data.collections[1].all_objects:
    if obj.type == 'CURVE':
        if obj.data.materials[0]:
            obj.data.extrude = 0.0004 + 0.001 * obj.data.materials[0].diffuse_color[0]
            obj.location[2] = obj.data.extrude * 100 #0.04 + 0.01 * obj.data.materials[0].diffuse_color[0]
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)
        bpy.ops.object.convert(target='MESH')
        obj.select_set(False)
    obj.scale[0] = 100
    obj.scale[1] = 100
    obj.scale[2] = 100

bpy.ops.export_mesh.stl(filepath=bpy.path.abspath("//test_map.stl"), check_existing=False)
