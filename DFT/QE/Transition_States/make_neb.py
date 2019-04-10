#!/usr/bin/env python
from ase import io
from ase.neb import NEB
import sys

# Read initial and final states:
initial = io.read('initial.traj') # copy relaxied ../IS/fin.traj as p0.traj
final = io.read('final.traj')   #copy relaxed ../FS/fin.traj as p6.traj
ni=7
try:
    ni=sys.argv[1]
except IndexError:
    print "generate band using 5 images"
# Make a band consisting of 5 images:
images = [initial]
images += [initial.copy() for i in range(ni-2)]
images += [final]
neb = NEB(images)
# Interpolate linearly the potisions of the three middle images:
neb.interpolate()

io.write('input_images.traj',images)
