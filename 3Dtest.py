
import open3d as o3d

# 3Dメッシュで表示
mesh = o3d.io.read_triangle_mesh("Bunny.ply")
o3d.visualization.draw_geometries([mesh])
print(mesh)

# 点群で表示
pointcloud = o3d.io.read_point_cloud("Bunny.ply")
o3d.visualization.draw_geometries([pointcloud])

# pcdデータをファイルに保存
o3d.io.write_point_cloud("Bunny.pcd", pointcloud)