import numpy as np    #vectors, matrices, lin. alg., etc.
import matplotlib
matplotlib.use('Agg') #turn off screen output so we can plot from the cluster
from ase.utils.eos import *  # Equation of state: fit equilibrium latt. const
from ase.units import kJ
from ase.lattice import bulk
from ase import *
from espresso import espresso

metal = 'Pt'
# if you have a metal alloy, specify the second metal as well
metal2 = None

a=3.97     #initial guess for lattice constant
strains = np.linspace(0.87, 1.13, 10) #range for scaling of latt. consts.
                                     #[0.87..1.13] in 10 steps

# if Mo then use bcc crystal, otherwise fcc
if metal == 'Mo':
  crystal = 'bcc'
else:
  crystal = 'fcc'

volumes = []  #we'll store unit cell volumes and total energies in these lists
energies = []
#setup up Quantum Espresso calculator
calc = espresso(pw=500, #plane-wave cutoff
                dw=5000,    #density cutoff
                xc='BEEF-vdW',    #exchange-correlation functional
                kpts=(11,11,11), #sampling grid of the Brillouin zone
                            #(is internally folded back to the
                                 #irreducible Brillouin zone)
                nbands=-10, #10 extra bands besides the bands needed to hold
                            #the valence electrons
                sigma=0.1,
                convergence= {'energy':1e-5,    #convergence parameters
                              'mixing':0.1,
                              'nmix':10,
                              'mix':4,
                              'maxsteps':500,
                              'diag':'david'
                              }, 
                psppath='/home/vossj/suncat/psp/gbrv1.5pbe',
                outdir='calcdir') #output directory for Quantum Espresso files

for i in strains: #loop over scaling factors
    #build Pt unit cell
    if metal2:
      atoms = bulk(metal, crystal, a=a*i, cubic=True)
      atoms.set_chemical_symbols(metal+'3'+metal2)
    else:
      atoms = bulk(metal, crystal, a*i)
    atoms.set_pbc((1,1,1))                #periodic boundary conditions about x,y & z
    atoms.set_calculator(calc)            #connect espresso to Pt unit cell
    volumes.append(atoms.get_volume())    #append the current unit cell volume
                                          #to list of volumes
    energy=atoms.get_potential_energy()   #append total energy to list of
    energies.append(energy)               #energies

eos = EquationOfState(volumes, energies) #Fit calculated energies at different
v0, e0, B = eos.fit()                    #lattice constants to an
                                         #equation of state

# setup bulk using optimized lattice and save it

if metal2:
  best_a = (v0)**(1./3.) # Angstroms
  atoms = bulk(metal, crystal, a=best_a, cubic=True)
  atoms.set_chemical_symbols(metal+'3'+metal2)
else:
  best_a = (4.*v0)**(1./3.) # Angstroms
  atoms = bulk(metal, crystal, best_a)
atoms.write('bulk.traj')

#output of lattice constant = cubic root of volume of conventional unit cell
#fcc primitive cell volume = 1/4 * conventional cell volume 
print 'Lattice constant:', best_a, 'AA'
print 'Bulk modulus:', B / kJ * 1e24, 'GPa'
print '(Fitted) total energy at equilibrium latt. const.:', e0, 'eV'
eos.plot(atoms.get_name()+'-eos.png')    #create a png plot of eos fit
