#!/usr/bin/env /home/vossj/suncat/bin/python

from ase.io import read
from ase.thermochemistry import HarmonicThermo
from ase.vibrations import Vibrations

########################################################################################################
## more information here: https://wiki.fysik.dtu.dk/ase/ase/thermochemistry/thermochemistry.html      ##
########################################################################################################

#########################################################################################################
#####                                     YOUR SETTINGS HERE                                        #####
#########################################################################################################

# rename to the name of your trajectory file
# containing the surface with adsorbates

atoms = read('qn.traj')

# name of output file for free energies
output_name = 'out.energy'

### At 300K and 101325 Pa
### change for your operating conditions
T = 300     # K
P = 101325  # Pa

#########################################################################################################
#####                                     END                                                       #####
#########################################################################################################

energy = atoms.get_potential_energy()                 # caclulate the energy, to be used to determine G
vibrateatoms = [atom.index for atom in atoms if atom.symbol in ['H','N']]   # calculate the vibrational modes for all N and H atoms
# Calculate vibrations
vib = Vibrations(atoms,indices=vibrateatoms,delta=0.03)    # define a vibration calculation
vib.run()                                                  # run the vibration calculation
vib.summary(method='standard')                             # summarize the calculated results

for mode in range(len(vibrateatoms)*3):                    # Make trajectory files to visualize the modes.
    vib.write_mode(mode)

vibenergies=vib.get_energies()
vibenergies=[vib for vib in vibenergies if not isinstance(vib,complex)]  # only take the real modes
gibbs = HarmonicThermo(vib_energies = vibenergies, electronicenergy = energy)

freeenergy = gibbs.get_gibbs_energy(T,P)

f=open(output_name,'w')
f.write('Potential energy: '+str(energy)+'\n'+'Free energy: '+str(freeenergy)+'\n')
f.close