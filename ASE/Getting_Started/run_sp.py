from ase import *
from espresso import espresso
from ase.lattice import bulk
import matplotlib
matplotlib.use('Agg') #turn off screen output so we can plot from the cluster
import matplotlib.pyplot as plt
import numpy as np


metal = 'Pt'
metal2 = None   # if you have an alloy, specify the second metal

name = metal
if metal2:
  name += metal2

a = 3.989  # optimized lattice constant

kpts = [6, 8, 10, 14, 18]   # list of k-points to try
energies = []

# if Mo then use bcc crystal, otherwise fcc
if metal == 'Mo':
  crystal = 'bcc'
else:
  crystal = 'fcc'

for k in kpts:
  if metal2:
    atoms = bulk(metal, crystal, a=a, cubic=True)
    atoms.set_chemical_symbols(metal+'3'+metal2)
  else:
    atoms = bulk(metal, crystal, a)

  calc = espresso(pw=500, #plane-wave cutoff
            dw=5000,    #density cutoff
            xc='BEEF-vdW',    #exchange-correlation functional
            kpts=(k,k,k), #sampling grid of the Brillouin zone
                        #(is internally folded back to the
                             #irreducible Brillouin zone)
            nbands=-10, #10 extra bands besides the bands needed to hold
                      #the valence electrons
            sigma=0.1,
            psppath='/home/vossj/suncat/psp/gbrv1.5pbe',  #pseudopotential path
            convergence= {'energy':1e-5,
                          'mixing':0.1,
                          'nmix':10,
                          'mix':4,
                          'maxsteps':500,
                          'diag':'david'
                         },  #convergence parameters
            outdir='calcdir') 

  atoms.set_pbc([1,1,1])      #periodic boundary conditions in all directions
  atoms.set_calculator(calc)  #connect espresso to Pt structure

  energy = atoms.get_potential_energy()  #this triggers a DFT calculation
  energies.append(energy)

  print 'k-points:', k, 'Total energy:', energy, 'eV'

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(kpts, energies)
ax.set_xlabel('k-points')
ax.set_ylabel('Total energy')
plt.tight_layout()
fig.savefig('kpts_vs_sp_energies.png')