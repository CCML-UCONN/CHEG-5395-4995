---
mathjax: false
permalink: /DFT/QE/Transition_States/
---

# ASE Tutorials
1. [Introduction to ASE](../)
2. [Getting Started](../Getting_Started/)
3. [Adsorption](../Adsorption/)
4. [Free Energy](../Free_Energy/)

____

## Transition State and Free Energy Calculations

In this final exercise, you will be calculating the transition state energy for N<sub>2</sub> dissociation using the fixed bond length (FBL) method. The  nudged elastic band (NEB) method can more accurately determine the saddle point for the transition state, but it is more computationally intensive and we won't be using it for this course. You will also be calculating the vibrational modes for the adsorbed species and using the modules within ASE to determine free energies. Finally, you will be putting everything together in order to calculate the reaction rate.


## Contents
3. [Vibrational Frequencies and Free Energies](#vibrational-frequencies)



### Required Files ###

Obtain the required files by running:

on Sherlock:

```bash
cd $SCRATCH
wget http://chemeng444.github.io/ASE/Transition_States/exercise_3_sherlock.tar
tar -xvf exercise_3_sherlock.tar
```

or on CEES:

```bash
cd ~/$USER
wget http://chemeng444.github.io/ASE/Transition_States/exercise_3_cees.tar
tar -xvf exercise_3_cees.tar
```


This will create a folder called `Exercise_3_Transition_States`.

<a name='fixed-bond-length-calculation'></a>

### Vibrational Frequencies and Free Energies ###

Calculate the vibrational frequencies for transition state and the final state using the [`run_freq.py`](run_freq.py) script. See the [ASE page](https://wiki.fysik.dtu.dk/ase/ase/thermochemistry/thermochemistry.html) for a detailed explanation of how this is implemented. Use `ase-gui` to view the vibrational modes, which are written out as `vib*.traj` files. There should be \\(3N\\) vibrational modes for all adsorbed states, and \\(3N - 1\\) vibrational modes for the transition state.

Since the fixed bond-length method cannot guarantee a solution at the saddle point (the image with the highest energy might not be exactly at the transition state), you may encounter multiple imaginary modes when you calculate the vibrational frequencies. In this case, the following scheme can be used:

* Any adsorbate should have \\(3N\\) non-imaginary vibrational modes
* Transition states should have \\(3N – 1\\) non-imaginary vibrational modes and one imaginary mode
* If there are extra imaginary modes replace < 7 meV with 7 meV

For the gas phase species, we will provide the results for N<sub>2</sub>, H<sub>2</sub>, and NH<sub>3</sub> for you. You calculated the results for N<sub>2</sub> in the last exercise and you can use either your own results or the one provided. These are in the `Gaseous_Molecules\` folder.

**<font color="red">Requirement:</font>** Calculate the vibrational frequencies for:

* Initial state: 2N\*
* Transition state: N-N\*
* Intermediates: N\*, NH\*, NH<sub>2</sub>\*, NH<sub>3</sub>\*,H\*

<a name='reaction-rate'></a>
