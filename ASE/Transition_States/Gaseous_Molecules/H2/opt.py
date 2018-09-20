#!/home/vossj/suncat/bin/python
#above line selects special python interpreter which knows all the paths
#SBATCH -p iric,normal,owners
#################
#set a job name
#SBATCH --job-name=H2_1
#################
#a file for job output, you can check job progress
#SBATCH --output=myjob.out
#################
# a file for errors from the job
#SBATCH --error=myjob.err
#################
#time you think you need; default is one hour
#in minutes in this case
#SBATCH --time=48:00:00
#################
#quality of service; think of it as job priority
#SBATCH --qos=normal
#################
#number of nodes you are requesting
#SBATCH --nodes=1
#################
#memory per node; default is 4000 MB per CPU
#SBATCH --mem-per-cpu=4000
#you could use --mem-per-cpu; they mean what we are calling cores
#################
#get emailed about job BEGIN, END, and FAIL
#SBATCH --mail-type=ALL
#################
#who to send email to; please change to your email
#SBATCH  --mail-user=colinfd@stanford.edu
#################
#task to run per node; each node has 16 cores
#SBATCH --ntasks-per-node=16
#################

from ase.data.molecules import molecule
from espresso import espresso
from ase.optimize import QuasiNewton
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
from ase.all import view,read,write

atoms = molecule('H2') # molecular
atoms.center(vacuum = 10.0)
atoms.set_cell([[10,0,0],[0,10.1,0],[0,0,10.2]])

calc = espresso(pw = 500.,
                dw = 5000.,
                nbands = -10,
            kpts=(1, 1, 1), 
            xc = 'BEEF', 
            outdir='outdir',
            psppath = "/scratch/users/colinfd/psp/gbrv",
            sigma = 10e-4)

atoms.set_calculator(calc)

dyn = QuasiNewton(atoms,logfile='out.log',trajectory='out.traj')
dyn.run(fmax=0.01) 
electronicenergy = atoms.get_potential_energy()

vib = Vibrations(atoms) # run vibrations on all atoms
vib.run()
vib_energies = vib.get_energies()

thermo = IdealGasThermo(vib_energies=vib_energies,
                        electronicenergy=electronicenergy,
                        atoms=atoms,
                        geometry='linear', # linear/nonlinear
                        symmetrynumber=2, spin=0) # symmetry numbers from point group

G = thermo.get_free_energy(temperature=300, pressure=101325.) # vapor pressure of water at room temperature

e = open('e_energy.out','w')
g = open('g_energy.out','w')
e.write(str(electronicenergy))
g.write(str(G))
