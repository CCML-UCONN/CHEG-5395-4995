---
layout: page
mathjax: false
permalink: /ASE/BEEF_DOS/
---

# ASE Tutorials
1. [Introduction to ASE](../)
2. [Getting Started](../Getting_Started/)
3. [Adsorption](../Adsorption/)
4. [Transition States](../Transition_States/)
5. [Error Estimation and Density of States](../BEEF_DOS/)

____

## Error Estimation and Density of States ##

## Contents
1. [Error Estimation Using BEEF](#BEEF)
2. [Projected Density of States](#DOS)

## Required Files ###

Obtain the required files by running:

on Sherlock:

```bash
cd $SCRATCH
wget http://chemeng444.github.io/ASE/BEEF_DOS/beef_dos_sherlock.tar
tar -xvf beef_dos_sherlock.tar
```

or on CEES:

```bash
cd ~/$USER
wget http://chemeng444.github.io/ASE/BEEF_DOS/beef_dos_cees.tar
tar -xvf beef_dos_cees.tar
```

This will create a folder called `BEEF_DOS`. Make a post on Piazza if you run into trouble.


<a name='BEEF'></a>

### Error Estimation Using BEEF ###

An example is provided in [`error_est.py`](error_est.py). To obtain the error on a quantity, such as the adsorption energy, you must first load in the results from the `.bee` files for each calculation. For N<sub>2</sub> dissociation that would be the calculations for N<sub>2 (g)</sub>, the cluster, and the 2N\*.

```python
E_N2, E_ens_N2 = read_beef('folder_name/N2.bee')
E_cluster, E_ens_cluster = read_beef('folder_name/cluster.bee')
E_2N_cluster, E_ens_2N_cluster = read_beef('folder_name/2N_cluster.bee')
```

Simply take the standard deviation of the ensemble values to get the "error" on the adsorption energy. For example, the adsorption energy can be obtained using


```python
E_2N = E_2N_cluster - E_cluster - E_N2
```

and then the standard deviation of the ensemble of 2N\* adsorption energies can be obtained using

```python
dE_2N = np.std(E_ens_2N_cluster - E_ens_cluster - E_ens_N2)
```

You may need to recalculate gas phase H<sub>2</sub> and NH<sub>3</sub> to obtain the associated `.bee` files.


<a name='DOS'></a>

### Projected Density of States ###

To obtain the projected density of states, first submit the [`pdos.py`](pdos.py) script after changing the settings to match your system. Then follow the instructions [here](https://github.com/vossjo/ase-espresso/wiki/Density-of-States).