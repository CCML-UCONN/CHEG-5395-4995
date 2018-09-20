from ase.dft.bee import BEEF_Ensemble
import numpy as np

ens = BEEF_Ensemble()

def read_beef(filename):
    energy, ensemble = ens.read(filename)
    return energy, ensemble


# read out the energy and the ensemble of energies for each calculation
E_N2, E_ens_N2 = read_beef('folder_name/N2.bee')
E_cluster, E_ens_cluster = read_beef('folder_name/cluster.bee')
E_2N_cluster, E_ens_2N_cluster = read_beef('folder_name/2N_cluster.bee')

# compute the energy
E_2N = E_2N_cluster - E_cluster - E_N2

# computer the standard deviation (the error) from the ensembles
dE_2N = np.std(E_ens_2N_cluster - E_ens_cluster - E_ens_N2)

print "Reaction energy:", E_2N
print "Error:", dE_2N