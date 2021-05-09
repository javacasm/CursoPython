import vtkplotlib as vpl
import numpy as np

# You can create a figure explicitly using figure()
fig = vpl.figure("Your Figure Title Here")

# Creating a figure automatically sets it as the current working figure
# You can get the current figure using gcf()
vpl.gcf() is fig # Should be True

# If a figure hadn't been explicitly created using figure() then gcf()
# would have created one. If gcf() had also not been called here then
# the plotting further down will have internally called gcf().

# A figure's properties can be edited directly
fig.background_color = "dark green"
fig.window_name = "A New Window Title"


points = np.random.uniform(-10, 10, (2, 3))

# To add to a figure you can either:

# 1) Let it automatically add to the whichever figure gcf() returns
vpl.scatter(points[0], color="r")

# 2) Explicitly give it a figure to add to
vpl.scatter(points[1], radius=2, fig=fig)

# 3) Or pass fig=None to prevent it being added then add it later
arrow = vpl.arrow(points[0], points[1], color="g", fig=None)
fig += arrow
# fig.add_plot(arrow) also does the same thing


# Finally when your ready to view the plot call show. Like before you can
# do this one of several ways
# 1) fig.show()
# 2) vpl.show() # equivalent to gcf().show()
# 3) vpl.show(fig=fig)

fig.show() # The program will wait here until the user closes the window.


# Once a figure is shown it is gets placed in `vpl.figure_history` which
# stores recent figures. The default maximum number of figures is two. For
# convenience whilst console bashing, you can retrieve the last figure.
# But it will no longer be the current working figure.

vpl.figure_history[-1] is fig # Should be True
fig is vpl.gcf() # Should be False

# A figure can be reshown indefinitely and should be exactly as you left it
# when it was closed.
fig.show()