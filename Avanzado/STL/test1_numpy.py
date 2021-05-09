import vtkplotlib as vpl
from stl.mesh import Mesh

# Read the STL using numpy-stl
mesh = Mesh.from_file('/home/javacasm/Descargas/Bearing_608_V02_tolMin.stl')

# Plot the mesh
vpl.mesh_plot(mesh)

# Show the figure
vpl.show()