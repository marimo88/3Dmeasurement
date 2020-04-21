
import open3d as o3d

# 3DメッシュをGUIで表示
mesh = o3d.io.read_triangle_mesh("Bunny.ply")
o3d.visualization.draw_geometries([mesh])
print(mesh)