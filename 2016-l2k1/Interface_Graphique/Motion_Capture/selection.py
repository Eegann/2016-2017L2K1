import bpy



def selec(a):
	arm = bpy.data.objects['Armature']
	bpy.ops.object.mode_set(mode='EDIT')
	bpy.ops.armature.select_all(action='DESELECT')
	bones_to_select = [a]
	for bone in arm.data.edit_bones:
		if bone.name in bones_to_select:
			bone.select = True
	bpy.ops.object.mode_set(mode='POSE')