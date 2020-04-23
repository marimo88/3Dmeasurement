
import open3d as o3d

# メッシュをバインディングボックスで囲う
bbox = o3d.geometry.AxisAlignedBoundingBox(min_bound=(-30, 0, -10),
                                               max_bound=(10, 20, 10))
mesh = o3d.io.read_triangle_mesh("Bunny.ply")
aabox = mesh.get_axis_aligned_bounding_box()
print(mesh)
o3d.visualization.draw_geometries([mesh,aabox])