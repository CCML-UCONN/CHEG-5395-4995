from ase.io import read
from ase.thermochemistry import IdealGasThermo


#################################################
# Script for calculating free energies of gases #
#################################################

## more information here: https://wiki.fysik.dtu.dk/ase/ase/thermochemistry/thermochemistry.html

#name your output
name = 'N2'

geometry = 'linear'

atoms = read('N2.traj')
#electronic energy in eV
energy = -553.610395

#vibrational energies in meV
vibenergies = [0, 0, 0, 7.6, 7.6, 299.2]

#convert from meV to eV for each mode
vibenergies[:] = [ve/1000. for ve in vibenergies]

#list of temperatures
temperatures = [298.15, 400, 500]

#operating pressure
pressures = [101325]

f=open(name+'_free.energy','w')
for temperature in temperatures:
    for pressure in pressures:
        gibbs = IdealGasThermo(vib_energies=vibenergies,
                                electronicenergy=energy,
                                atoms=atoms,
                                geometry=geometry,
                                symmetrynumber=2, spin=0)
        freeenergy = gibbs.get_gibbs_energy(temperature,pressure)
        f.write('Temperature: '+str(temperature)+'\t'+'Pressure: '+str(pressure)+'\t'+'Free energy: '+str(freeenergy)+'\n')
        

f.close
