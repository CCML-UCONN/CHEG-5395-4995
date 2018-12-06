from ase import *
from ase.lattice.surface import *
from ase.lattice.surface import surface
from ase.optimize import *
from ase.constraints import *
from ase import io

#create a (111) or (110) surface slab of 2x2x4
#(2x2) surface area; 3 layers along surface normal)
#7 angstrom vacuum layer added on each side

# run this from the directory where you finished the lattice optimization

metal = 'Pt'
# if you have a metal alloy, specify it here
metal2 = None

# your OPTIMIZED lattice constant
# for alloys, the setup will use your optimized trajectory directly
a = 3.989    

vacuum = 7.0
layers = 4
if metal2:
    bulk = io.read('../Bulk/bulk.traj')    # TODO: change this path to the optimized bulk.traj alloy
    if metal == 'Mo':
        slab = surface(bulk, (1,1,0), layers, vacuum=vacuum)
    else:
        slab = surface(bulk, (1,1,1), layers, vacuum=vacuum)
else:
    if metal == 'Mo':
        slab = bcc110(metal, a=a, size=(2,2,layers), vacuum=vacuum)
    else:
        slab = fcc111(metal, a=a, size=(2,2,layers), vacuum=vacuum)

# mask for atoms with z-axis less than 10 A
# set constraint to Fix Atoms

# TODO: check to make sure that only the bottom two layers are fixed
mask = [atom.z<10.0 for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))

fixatoms = FixAtoms(mask=mask)
slab.set_constraint(fixatoms) #fix everything but the top layer atoms
slab.rattle()                 #define random displacements to

slab.write('slab.traj')
