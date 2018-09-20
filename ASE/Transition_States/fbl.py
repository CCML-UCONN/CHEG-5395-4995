import sys
import cPickle as pickle

from ase import *
from ase import io
from ase.constraints import FixAtoms, FixBondLength
from ase.dft.bee import BEEF_Ensemble
from ase.optimize import QuasiNewton
from espresso import espresso

#########################################################################################################
#####                                     YOUR SETTINGS HERE                                        #####
#########################################################################################################

# read in trajectory. this should be with the two dissociated N atoms
atoms = io.read('surface.traj')

# specify the two N atoms whose distance is to be fixed
# during the geometry optimization
# MAKE SURE YOU HAVE CHOSEN THE RIGHT ATOMS BEFORE SUBMITTING
# don't wait until it has finished running to find out you fixed
# the wrong atoms

atom1=12
atom2=13

# SET TO True if fix cluster, otherwise False
fix_cluster = True

# FOR SURFACES, set to the height below which atoms are fixed.
# This is needed as the fixed bong length is a constraint and all of them need to be set again
# if your system is a cluster, this setting will be ignored
z_height = 10.0

# threshold bond-length for terminating the FBL calculation
threshold = 0.9

## CORRECT KPTS SET AUTOMATICALLY

#########################################################################################################
#####                                     END                                                       #####
#########################################################################################################


# apply all constraints
constraints = [FixBondLength(atom1,atom2)]

metal_atoms = [atom.index for atom in atoms if atom.symbol not in ['N','H']]
num_atoms = len(metal_atoms)


### NO NEED TO DO ANYTHING HERE ###
# the if conditions take care of everything
# checks which type of system it is and sets the right constraints

if num_atoms == 16:
    print "slab calculation..."
    kpts = (4, 4, 1)
    mask = [atom.z < z_height for atom in atoms]      # atoms in the structure to be fixed
    constraints.append(FixAtoms(mask=mask))
elif  num_atoms == 13:
    print "cluster calculation..."
    kpts = 'gamma'
    if fix_cluster:
        constraints.append(FixAtoms(indices=metal_atoms))
else:
    print "Wrong number of metal atoms! Check your input trajectory!"
    exit()


# apply constraints - always use this unless NO atoms are fixed
atoms.set_constraint(constraints)


# Find the distance between the two atoms to fix
a = Atoms()
a.append(atoms[atom1])
a.append(atoms[atom2])
d = a.get_distance(0,1)
        
# calculator setup, using the same settings as before
calc = espresso(pw = 500,
                dw = 5000,
                kpts = kpts,     # (4,4,1) FOR SURFACES and 'gamma' FOR CLUSTERS
                nbands = -10,
                xc = 'BEEF-vdW', 
                psppath='/home/vossj/suncat/psp/gbrv1.5pbe',
                convergence = {'energy':1e-5,
                               'mixing':0.1,
                               'nmix':10,
                               'maxsteps':500,
                               'diag':'david'
                                },
                beefensemble=True,
                spinpol = False,
                outdir = 'calcdir',
                )   

# attach the calculator
atoms.set_calculator(calc)

# Print the results to a file called "PES.dat"
# this will write out the total energy at each fixed bond length
f = open('PES.dat', 'w')
print >> f,'newlength energy'

# number of steps
numsteps = 40

# for loop that changes the distance between the atoms, fixes it, and performs
# a structural optimization. results writen out as i*.traj files
for step, delta in enumerate(xrange(0,30,1)):
    if atoms.get_distance(atom1, atom2) < threshold:
        break

    if step < numsteps:
        atoms.set_distance(atom1, atom2, d, fix=0.5)

        qn = QuasiNewton(atoms, trajectory='i'+str(delta)+'.traj')
        qn.run(fmax=0.05)
        
        e = atoms.get_potential_energy()

        print d, e
        print >> f, d, e
        f.flush()
        
    d -= 0.1

f.close()

# ensemble
ens = BEEF_Ensemble(calc)
ens.get_ensemble_energies()
ens.write('fbl.bee')
del sys, calc, ens
