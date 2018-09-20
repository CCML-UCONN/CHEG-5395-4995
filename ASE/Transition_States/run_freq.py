from ase.constraints import FixAtoms
from ase.io import read
from ase.thermochemistry import HarmonicThermo
from ase.vibrations import Vibrations
from espresso import espresso
from espresso.vibespresso import vibespresso

########################################################################################################
## more information here: https://wiki.fysik.dtu.dk/ase/ase/thermochemistry/thermochemistry.html      ##
########################################################################################################

#########################################################################################################
#####                                     YOUR SETTINGS HERE                                        #####
#########################################################################################################

# rename to the name of your trajectory file
# containing the surface with adsorbates

atoms = read('ads_surface.traj')

#########################################################################################################
#####                                     END                                                       #####
#########################################################################################################

metal_atoms = [atom.index for atom in atoms if atom.symbol not in ['N','H']]
num_atoms = len(metal_atoms)

if num_atoms == 16:
  kpts = (4, 4, 1)
elif  num_atoms == 13:
  kpts = 'gamma'
else:
  print "Wrong number of metal atoms! Check your input trajectory!"
  exit()

params = {'pw':500,
          'dw':5000,
          'kpts':kpts,
          'nbands':-20,
          'xc':'BEEF-vdW',
          'psppath':'/home/vossj/suncat/psp/gbrv1.5pbe',
          'convergence':{'energy':1e-5, 'mixing':0.1, 'nmix':10, 'maxsteps':500, 'diag':'david'},
          'spinpol':False}


calc = espresso(outdir = 'calcdir', **params)             # regular espresso calculator
calcvib = vibespresso(outdirprefix = 'vibdir', **params)  # special calculator for the vibration calculations

atoms.set_calculator(calc)                            # attach calculator to the atoms                   

energy = atoms.get_potential_energy()                 # caclulate the energy, to be used to determine G

# vibrate N and H atoms
vibrateatoms = [atom.index for atom in atoms if atom.symbol in ['H','N']]   # calculate the vibrational modes for all N and H atoms
atoms.set_calculator(calcvib)                                             # attach vibrations calculator to the atoms                   

# Calculate vibrations                                                                                        
vib = Vibrations(atoms,indices=vibrateatoms,delta=0.03)    # define a vibration calculation                   
vib.run()                                                  # run the vibration calculation                    
vib.summary(method='standard')                             # summarize the calculated results                 

for mode in range(len(vibrateatoms)*3):                    # Make trajectory files to visualize the modes.    
    vib.write_mode(mode)


### UNCOMMENT TO CALCULATE FREE get_energies

### YOU CAN ALSO USER get_ads_free_energy.py and get_gas_free_energy.py
### Calculate free energy

# vibenergies=vib.get_energies()
# vibenergies=[vib for vib in vibenergies if not isinstance(vib,complex)]  # only take the real modes
# gibbs = HarmonicThermo(vib_energies = vibenergies, electronicenergy = energy)

### At 300K and 101325 Pa
### change for your operating conditions 

# freeenergy = gibbs.get_gibbs_energy(300,101325)

# f=open('out.energy','w')
# f.write('Potential energy: '+str(energy)+'\n'+'Free energy: '+str(freeenergy)+'\n')
# f.close