import vtkplotlib as vpl
from stl.mesh import Mesh

# path = "if you have an STL file then put it's path here."
# Otherwise vtkplotlib comes with a small STL file for demos/testing.
path = vpl.data.get_rabbit_stl()

# Read the STL using numpy-stl
mesh = Mesh.from_file(path)

# Plot the mesh
vpl.mesh_plot(mesh)

# Show the figure
vpl.show()