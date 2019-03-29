import os
import sys
from ase.io import read
from ase.constraints import *


if len(sys.argv) < 1:
    print "Usage: python replace_with_fixed_cluster.py file.traj"
    exit()

atoms = read(sys.argv[1])
metals = atoms.get_chemical_symbols()[:2]
if len(set(metals)) < 2:
    del metals[1]

hostname = os.environ.get('HOSTNAME')
username = os.environ.get('USER')

if 'cees' in hostname:
    tmpdir = '/data/cees/'+username
elif 'sherlock' in hostname:
    tmpdir = os.environ.get('SCRATCH')

catalyst = ''.join(metals)

if not os.path.exists(tmpdir+"/Fixed_"+catalyst+".traj"):
    os.system("wget http://chemeng444.github.io/Fixed_Lattice_Clusters/"+catalyst+".traj -O "+tmpdir+"/Fixed_"+catalyst+".traj")

fixed_cluster = read(tmpdir+"/Fixed_"+catalyst+".traj")
fixed_cluster.set_cell(atoms.cell)
fixed_cluster.center()

atoms.set_constraint()
del atoms[[atom.index for atom in atoms if atom.symbol in metals]]

atoms += fixed_cluster
atoms.set_constraint(FixAtoms(indices=[atom.index for atom in atoms if atom.symbol in metals]))
atoms.write(sys.argv[1])