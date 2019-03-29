---
mathjax: true
permalink: /DFT/QE/Getting_Started/
---

# ASE Tutorials
1. [Introduction to ASE](../)
2. [Getting Started with DFT Calculations__HW3a](../Getting_Started/)
3. [Adsorption_HW3b](../Adsorption/)

____

## Getting Started with DFT Calculations ##

In the first exercise, we will be studying how to determine the interaction between the Pt(111) and an adsorbate. For Homework 3, We will first optimize the structure of Pt(111) clean surface and calculate its energy. In [part b](../Adsorption/) you will calculate the CO and O adsorption energies on Pt(111) following similar procedures.

## Contents ##

1. [A Typical ASE Script](#a-typical-ase-script)
<a name='a-typical-ase-script'></a>

### A Typical ASE Script ###

ASE scripts can be run directly in the terminal (in the login node) or submitting to external nodes. Generally, you will be submitting jobs to external nodes and only small scripts will be run on the login node. By default, all output from any submitted script will be written *from the directory where the submission command was executed*, so make sure you are inside the calculation folder before running the submission command.

There are two files that are necessary to run jobs on the HPC-Storrs cluster. You can copy an example from `/home/liz18025/shared/hw3`. The first is `esp.sub`; this is the file that tells the scheduler how much time the job is allowed, how many processors it requires, and other pertinent information. First, notice the comments in the beginning. These include information such as how much time to allocate, the number of nodes required, what the names of the output and error files are, what the name of the job should be, and what your email is.

```bash
#!/bin/sh
#SBATCH --partition=general_requeue                   # Name of partition
#SBATCH --ntasks=24                           # Request 24 CPU cores
#SBATCH --nodes=1
#SBATCH --time=6:00:00                       # Job should run for up to 2 hours (for example)
#SBATCH --mail-type=END                      # Event(s) that triggers email notification (BEGIN,END,FAIL,ALL)
#SBATCH --mail-user=YourEmail      # Destination email address
##SBATCH --exclude=cn[01-136,325-328]
#SBATCH -o out.%j
#SBATCH -e err.%j

module unload ase qe
module load ase
module load qe/pybf

which pw.x
cd $SLURM_SUBMIT_DIR
export OMP_NUM_THREADS=1
python ./qe-opt.py
```

Finally, the last line ```python qe-opt.py``` picks the script you want to run. Therefore, you need to change the name of the file depending on which script you are running.


Let's look at how a typical ASE script is written. Open the [`qe-opt.py`](energy.py) script. We import all the relevant ASE modules in for this calculation

```python
from espresso import espresso
from ase.io import read, write
```

`from espresso import espresso` imports the Quantum ESPRESSO calculator for the ASE interface, and `from ase.io import read, write` imports the read and write commands for trajectory files.

An existing trajectory can be read in:

```python
# read in the slab
posin=read("init.traj")       #change the name of .traj file accordingly
slab=posin.copy()
```

Then, the Quantum ESPRESSO calculator is set up. All parameters related to the electronic structure calculation are included here. The following example shows typical parameters that we use in the group for MXene calculations.

```python
convergence = {'energy':1e-5,
                'mixing':0.3,
                'nmix':10,
                'maxsteps':500,
                'diag':'david'
                }

output = {'avoidio':False,
        'removewf':True,
        'wf_collect':False}

calc = espresso(pw=500 , # Plane wave cutoff
    dw=5000, # Density wave cutoff
    spinpol=False,
    nbands=-50,
    smearing='gauss',
    sigma=0.1,
    kpts=(4,4,1), # (rather sparse) k-point (Brillouin) sampling
    xc='RPBE', #Exchange-correlation functional
    dipole={'status':True}, # Includes dipole correction (necessary for asymmetric slabs)
    parflags='-npool 1',
    convergence=convergence,
    outdir = 'esplog',
    output = output,) # Espresso-generated files will be put here
```

Finally, the Quantum ESPRESSO calculator is attached to the `slab` Atoms object, the energy calculation is ran, and the total energy of the system is output in the log file (defined in the `esp.sub` file above).

To submit the job, use:

```bash
sbatch -J $PWD esp.sub

```
The `-J $PWD` gives the name of the job as the current directory. Make sure this calculations runs correctly before proceeding.

Once you job started, you will see multiple new files created in the directory you submitted your jobs. In the file `relax.log` you will find output like this (numbers could be different):
```
Step     Time          Energy         fmax
BFGS:    0 11:01:08   -15824.569925        0.7996
BFGS:    1 11:02:00   -15824.604684        0.6934
BFGS:    2 11:03:07   -15824.689232        0.3910
BFGS:    3 11:04:13   -15824.739921        0.4943
....
```

The first column tells us we are using a Broyden–Fletcher–Goldfarb–Shanno (BFGS) algorithm to optimize the atomic positions. The second column is the step number (the first step before we move atoms at all is 0). The third column tells us the time each ionic step is calculated, the fourth column is the total energy of the system (eV), and the last column is the maximum force on an atom (eV/Å).
