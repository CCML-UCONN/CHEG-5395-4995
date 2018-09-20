from ase import *
from ase import io
from ase.lattice.surface import *
from ase.optimize import *
from ase.constraints import *
from espresso import espresso

metal = 'Pt111'
name = metal

# read in the slab
slab = io.read('slab.traj')

# height below which to fix the slab, view your trajectory to confirm this
fix_z_height = 10.0

#espresso calculator setup
calc = espresso(pw=500,           #plane-wave cutoff
                dw=5000,          #density cutoff
                xc='BEEF-vdW',    #exchange-correlation functional
                kpts=(4,4,1),     #k-point sampling;
                                  #no dispersion to be sampled along z
                nbands=-10,       #10 extra bands besides the bands needed to hold
                                  #the valence electrons
                sigma=0.1,
                psppath='/home/vossj/suncat/psp/gbrv1.5pbe',    #pseudopotential path
                convergence= {'energy':1e-5,
                              'mixing':0.1,
                              'nmix':10,
                              'mix':4,
                              'maxsteps':500,
                              'diag':'david'
                             },  #convergence parameters
                outdir='calcdir') #output directory for Quantum Espresso files

mask = [atom.z < fix_z_height for atom in slab]      # atoms in the structure to be fixed
fixatoms = FixAtoms(mask=mask)
slab.set_constraint(fixatoms)               # fix everything but the top layer atoms
slab.rattle()                               # define random displacements to the atomic positions before optimization

slab.set_calculator(calc)                       #connect espresso to slab
qn = QuasiNewton(slab, trajectory=name+'.traj', logfile=name+'.log') #relax slab
qn.run(fmax=0.05)                               #until max force<=0.05 eV/AA
