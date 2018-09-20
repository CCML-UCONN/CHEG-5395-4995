#!/usr/bin/env /home/vossj/suncat/bin/python
#SBATCH -p iric 
#SBATCH --job-name=clusters
#SBATCH --output=clusters.out
#SBATCH --error=clusters.err
#SBATCH --time=2880:00
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=4000
#SBATCH --mail-type=ALL
#SBATCH --mail-user=ctsai89@stanford.edu
#SBATCH --ntasks-per-node=16


import numpy as np
import os
from ase import Atoms
from ase.cluster.octahedron import Octahedron
from espresso import espresso
from numpy import *
from scipy.optimize import fmin


lc = 3.9    # starting guess for lattice

element1 = #ELEMENT1
element2 = #ELEMENT2

name = element1 + element2

if not os.path.exists(name):
    os.makedirs(name)

def make_cluster(element1,element2,a):
    atoms = Octahedron(element1, length=3, cutoff=1, latticeconstant=float(a))
    atoms.center(vacuum=7.0)

    # if there is a second element, swap out 6 of the atoms for the other metal
    if element2:
        for i in range(1,len(atoms),2):
            atoms[i].symbol = element2

    return Atoms(atoms)

def get_energy(x):
    global iteration
    iteration +=1
    
    atoms = make_cluster(element1,element2,x)

    calc = espresso(pw=500,
                dw=5000,
                xc='BEEF-vdW',
                kpts='gamma',
                nbands=-20,
                sigma=0.1,
                convergence = {'energy':0.0005,
                               'mixing':0.1,
                               'nmix':10,
                               'maxsteps':500,
                               'diag':'david',
                               },
                outdir='calcdir_'+str(iteration),
                )

    atoms.set_calculator(calc)
    energy = atoms.get_potential_energy()
    
    print('%20.8f%20.8f' % (x,energy))
    
    f = open('out%04i.energy' % iteration, 'w')
    f.write(repr(x) + ' ' + str(energy))
    f.close()
    
    # cleanup
    calc.stop()
    del calc
    os.system('rm -r calcdir_'+str(iteration))

    return energy

print name
print('%20s%20s' % ('a','energy'))
iteration = 0.

x = fmin(get_energy, x0=lc, xtol=0.001, ftol=0.00001)
print('Best lc')
print x
best_atoms = make_cluster(element1,element2,x)
best_atoms.write(name+'.traj')