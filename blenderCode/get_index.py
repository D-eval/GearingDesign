import bpy
import bmesh

def get_index():
    obj = bpy.context.object
    mesh = obj.data
    # 确保是在编辑模式
    if obj.mode != 'EDIT':
        bpy.ops.object.mode_set(mode='EDIT')
    # 获取 BMesh
    bm = bmesh.from_edit_mesh(mesh)
    # 确保可以通过索引访问
    bm.verts.ensure_lookup_table()
    # 获取所有选中的顶点索引
    selected_indices = [v.index for v in bm.verts if v.select]
    print("选中的顶点索引：", selected_indices)
