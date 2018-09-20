from ase.thermochemistry import HarmonicThermo


######################################################
# Script for calculating free energies of adsorbates #
######################################################

## more information here: https://wiki.fysik.dtu.dk/ase/ase/thermochemistry/thermochemistry.html

name = 'example_ads'

#electronic energy in eV
energy = -21861.531796 

#vibrational energies in meV
vibenergies = [60.5, 77.1, 314.2]

#convert from meV to eV for each mode
vibenergies[:] = [ve/1000. for ve in vibenergies]

#list of temperatures
temperatures = [300]

#operating pressure
pressures = [101325]

f=open(name+'_free.energy','w')
for temperature in temperatures:
    for pressure in pressures:
        gibbs = HarmonicThermo(vib_energies = vibenergies, electronicenergy = energy)
        freeenergy = gibbs.get_gibbs_energy(temperature,pressure)
        f.write('Temperature: '+str(temperature)+'\t'+'Pressure: '+str(pressure)+'\t'+'Free energy: '+str(freeenergy)+'\n')
        

f.close
