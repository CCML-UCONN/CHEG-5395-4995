from ase import Atoms
from ase.cluster.octahedron import Octahedron
from ase.cluster.icosahedron import Icosahedron

# script for setting up M13 cluster

# replace with your assigned element and your optimized lattice parameter
# if your assigned system is a binary alloy, specify element2 (e.g. 'Cu')
element1 = 'Pt'
element2 = None		# change to 'Cu' for example if you have an alloy
a = None            # optionally specify a lattice parameter
vacuum = 7.0

# create the cluster and add vacuum around the cluster
# we use cuboctahedrons here, though other shapes are possible

atoms = Octahedron(element1, length=3,cutoff=1)
#atoms = Icosahedron(element1, noshells=2)
atoms.center(vacuum=vacuum)


# if there is a second element, swap out 6 of the atoms for the other metal
if element2:
    for i in range(1,len(atoms),2):
        atoms[i].symbol = element2

# write out the cluster
Atoms(atoms).write('cluster.traj')