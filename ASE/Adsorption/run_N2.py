import cPickle as pickle

from ase import *
from ase import io
from ase.dft.bee import BEEF_Ensemble
from ase.optimize import QuasiNewton
from ase.structure import molecule
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
from espresso import espresso
from espresso.vibespresso import vibespresso

name = 'N2'

# load N2 molecule and add 20.0 AA vacuum
atoms = molecule('N2')
atoms.center(10.0)

calc = espresso(pw=500,        # plane-wave cutoff
                dw=5000,       # density cutoff
                xc='BEEF-vdW',  # exchange-correlation functional
                kpts='gamma',  # k-point sampling
                nbands=-10,    # 10 extra bands besides the bands needed to hold
                               # the valence electrons
                sigma=0.1,
                psppath='/home/vossj/suncat/psp/gbrv1.5pbe',  # pseudopotential
                convergence={'energy': 1e-5,
                             'mixing': 0.1,
                             'nmix': 10,
                             'mix': 4,
                             'maxsteps': 500,
                             'diag': 'david'
                             },    # convergence parameters
                beefensemble=True,
                printensemble=True,
                outdir='calcdir')  # output directory for Quantum Espresso files

atoms.set_calculator(calc)

vibrateatoms = [atom.index for atom in atoms]

dyn = QuasiNewton(atoms, logfile=name + '.log', trajectory=name + '.traj')
dyn.run(fmax=0.05)

energy = atoms.get_potential_energy()

calc.stop()

# Calculate vibrations
calcvib = vibespresso(pw=500,         # plane-wave cutoff
                      dw=5000,        # density cutoff
                      xc='BEEF-vdW',  # exchange-correlation functional
                      kpts='gamma',   # k-point sampling
                      nbands=-10,     # 10 extra bands besides the bands needed to hold
                                      # the valence electrons
                      sigma=0.1,
                      psppath='/home/vossj/suncat/psp/gbrv1.5pbe',  # pseudopotential
                      convergence={'energy': 1e-5,
                                   'mixing': 0.1,
                                   'nmix': 10,
                                   'mix': 4,
                                   'maxsteps': 500,
                                   'diag': 'david'
                                   },  # convergence parameters
                      outdirprefix='calcdirv')  # output directory for Quantum Espresso files

atoms.set_calculator(calcvib)


vib = Vibrations(atoms, indices=vibrateatoms, delta=0.03)
vib.run()
vib.summary(method='standard')

# Make trajectory files to visualize the modes.
for mode in range(len(vibrateatoms) * 3):
    vib.write_mode(mode)

# Calculate free energy
vib_energies = vib.get_energies()
thermo = IdealGasThermo(vib_energies=vib_energies,
                        electronicenergy=energy,
                        atoms=atoms,
                        geometry='linear',
                        symmetrynumber=2, spin=0)

# At 300K and 101325 Pa
# change for your operating conditions
freeenergy = thermo.get_gibbs_energy(temperature=300, pressure=101325)

f = open(name + '.energy', 'w')
f.write('Potential energy: ' + str(energy) + '\n' +
        'Free energy: ' + str(freeenergy) + '\n')
f.close

ens = BEEF_Ensemble(calc)
ens_e = ens.get_ensemble_energies()
ens.write('ensemble.bee')
pickle.dump(ens_e, open('ensemble.pkl', 'w'))
