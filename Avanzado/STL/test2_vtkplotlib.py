import vtkplotlib as vpl
from stl.mesh import Mesh

# Open an STL as before
path = vpl.data.get_rabbit_stl()
mesh = Mesh.from_file(path)

# Plot it with the z values as the scalars. scalars is 'per vertex' or 1
# value for each corner of each triangle and should have shape (n, 3).
plot = vpl.mesh_plot(mesh, scalars=mesh.z)

# Optionally the plot created by mesh_plot can be passed to color_bar
vpl.color_bar(plot, "Heights")

vpl.show()