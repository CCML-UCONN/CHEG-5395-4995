from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import QuasiNewton
from ase.io import read, write

IS = read('H2.traj')
IS.set_calculator(EMT())
qn = QuasiNewton(IS, trajectory='initial.traj')
qn.run(fmax=0.01)


FS = read('2H.traj')
FS.set_calculator(EMT())
qn = QuasiNewton(FS, trajectory='final.traj')
qn.run(fmax=0.01)


