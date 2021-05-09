import vtkplotlib as vpl
from stl.mesh import Mesh
import numpy as np

# Open an STL as before
path = vpl.data.get_rabbit_stl()
mesh = Mesh.from_file(path)

# `tri_scalars` must have one value per triangle and have shape (n,) or (n, 1).
# Create some scalars showing "how upwards facing" each triangle is.
tri_scalars = np.inner(mesh.units, np.array([0, 0, 1]))

vpl.mesh_plot(mesh, tri_scalars=tri_scalars)

vpl.show()