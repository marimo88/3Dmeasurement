
import copy
import open3d as o3d
import numpy as np

mesh = o3d.io.read_triangle_mesh("Bunny.ply")
mesh.compute_vertex_normals()
mesh1 = copy.deepcopy(mesh)

# データの前半のメッシュデータだけを抽出
mesh1.triangles = o3d.utility.Vector3iVector(
        np.asarray(mesh1.triangles)[:len(mesh1.triangles) // 2, :])
mesh1.triangle_normals = o3d.utility.Vector3dVector(
        np.asarray(mesh1.triangle_normals)[:len(mesh1.triangle_normals) //  2, :])

# 加工後データ表示
print(mesh1)
o3d.visualization.draw_geometries([mesh1])