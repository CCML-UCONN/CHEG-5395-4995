from ase import io
from ase.lattice.surface import add_adsorbate, fcc111, bcc110

# name of output trajectory file

# lattice constant for fcc Pt
name = 'N+N_Pt'

# read in your optimized surface or cluster
slab = io.read('surface.traj')


# add adsorbate using add_adsorbate(surface,symbol,z,(x,y))
# where "surface" is the object containing the surface, "slab" in this case
# and z is the position above the surface (from the center of the top most atom)
# and x and y are the absolute coordinates

# add two neighboring N atoms:
add_adsorbate(slab, 'N', 1.5, (3, 1.7))
add_adsorbate(slab, 'N', 1.5, (1.5, 0.86))

## If you are setting up the slab using the built in fcc111 or bcc110 functions, you can also directly specify the site name
## though you can only add one adsorbate per type of site with this function. e.g.,
# slab = fcc111(metal, a = a, size = (2,2,4), vacuum = 7.0)
# add_adsorbate(slab, 'N', 1.5, 'ontop')
# add_adsorbate(slab, 'N', 1.5, 'slab')

# use ag to view the slab and find the right x,y position

# save the trajectory file
slab.write(metal+'N+N.traj')