#!/usr/bin/env /home/vossj/suncat/bin/python

## your job name
#PBS -N job_name
#PBS -l nodes=1:ppn=4
#PBS -l walltime=20:00:00
#PBS -q Q19
#PBS -V
#PBS -m e
#PBS -W x="PARTITION:sw121"

## your email address
#PBS -M sunetid@stanford.edu

## names for the job outputs
#PBS -e myjob.err
#PBS -o myjob.out

# **IMPORTANT** make sure number of nodes matches images. i.e. for 5 images:
# #SBATCH --nodes=5
# or
# #PBS -l nodes=5:ppn=4


###############
#More details about NEB here: https://wiki.fysik.dtu.dk/ase/ase/neb.html
###############

from ase import io
from ase.optimize import BFGS as QuasiNewton
from ase.optimize import FIRE
from ase.neb import NEB
from espresso.multiespresso import multiespresso
import numpy as np

xc = 'BEEF-vdW'

intermediate_images = 5

#set up multiple espresso calculators
#example shown here: slabs: dipole correction is turned on
m = multiespresso(ncalc=intermediate_images,outdirprefix='ekspressen',
                  pw=500.,
                  dw=5000.,
                  xc=xc,
                  kpts=(4,4,1),
                  nbands=-20,
                  spinpol=False,
                  psppath='/home/vossj/suncat/psp/gbrv1.5pbe',
                  dipole={'status':True},
                  output = {'avoidio':True,'removewf':True,'wf_collect':False},
                  convergence={'energy':1e-5,'mixing':0.25,'maxsteps':300})


# these trajectories have to contain total energies and forces besides the coordinates
# you must perform a structural optimization on them first and then use the results here
initial = io.read('neb0.traj')
final = io.read('neb6.traj')

# read in the intermediate images and attach them in a list
images = [initial]
for img_num in np.arange(1,intermediate_images+1,1):
	images.append(io.read('neb%d.traj' % img_num)) 
images.append(final)

# set up the NEB object 
neb = NEB(images)
m.set_neb(neb)

# setup and run the relaxation for the reaction path
qn = QuasiNewton(neb, logfile='qn.log')

for j in range(1,intermediate_images+1):
    traj = io.PickleTrajectory('neb%d.traj' % j, 'w', images[j])
    qn.attach(traj)

qn.run(fmax=0.05)
