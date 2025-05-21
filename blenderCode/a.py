import bpy
import bmesh
import mathutils

# 相对偏移向量
offset = mathutils.Vector((10.0, 5.0, 0.0))

# 获取当前对象
obj = bpy.context.object
mesh = obj.data

# 建立顶点索引 → 顶点组名 映射
def get_vert_index_by_group(obj, group_name):
    group_idx = obj.vertex_groups[group_name].index
    for v in obj.data.vertices:
        for g in v.groups:
            if g.group == group_idx:
                return v.index
    return None

# 找到两个顶点索引
idx_ref = get_vert_index_by_group(obj, "ref_point")
idx_target = get_vert_index_by_group(obj, "target_point")

obj.data.vertices[idx_ref]


# 用 BMesh 修改顶点坐标
bm = bmesh.new()
bm.from_mesh(mesh)

bm.verts.ensure_lookup_table()
v_ref = bm.verts[idx_ref]
v_target = bm.verts[idx_target]

v_target.co = v_ref.co + offset
print(f"设置 target_point = ref_point + {offset}")

bm.to_mesh(mesh)
bm.free()
