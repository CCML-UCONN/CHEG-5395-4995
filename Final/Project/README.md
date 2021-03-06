---
mathjax: true
permalink: /Final/Project/
published: true
---
* [Homepage](/CHEG-5395-4995/)
# Final Project #
1. [Teams and Timeline](/CHEG-5395-4995/Final/Team/)
2. [Project Description](/CHEG-5395-4995/Final/Project/)

________

## Project Description ##
1. [Ion-exchanged Zeolite for Gas Separation ](#separation)
2. [Design of SnO2-based Oxygen Evolution Reaction (OER) Catalysts](#oer)
3. [Q and A](#qanda)

<a name='separation'></a>
## Zeolite for Gas Separation ##
Path:`/home/liz18025/shared/cheg4995-5395/final_project/Separation`

In this project, you will be calculating the adsorption free energy of Benzene(C6H6) and Thiophene (C4H4S) on the larges pore of the ZSM-5 zeolite. Due to the limitation of the computation resource, you will perform the calculation on the cut-out model, which consist of the 10-Si-atom ring(pore) and necessary surrounding atoms.

<center><img src="Images/centered_traj_0.png" alt="add" style="width: 300px;"/><br>
10-Si-atom Ring
</center>

Your tasks include the following:
* Using `make_ring.py` to generate a proper model for Zeolite simulation by adjusting the `cutoff` value. Make sure your structure has the same stoichiometry as SiO2 to avoid electronic converging issue. Optimize its structure with by fixing surrounding atoms.

* Calculate the adsorption free energy of Benzene and Thiophene on the 10-Si-atom ring of the pure ZSM-5.
<center>
<img src="Images/benzene.png" alt="add" style="height: 250px;"/>
<img src="Images/Thiophene.png" alt="add" style="height: 250px;"/>
<br>
Benzene and Thiophene
</center>

* Calculate adsorption free energy of Benzene and Thiophene on the 10-Si-atom ring of the ion-exchanged ZSM-5

* Discuss how the adsorption isotherm (separation ability) is affected by ion-exchange.

<a name='oer'></a>
## SnO2-based OER Catalysts ##
Path:`/home/liz18025/shared/cheg4995-5395/final_project/OER`

Pure SnO2 itself is one of the worst OER catalysts, due to weak binging of O species on the surface. You will be calculating the adsorption free energy of O and OH on pure and doped SnO2(110) surface to obtain the theoretical OER over-potential. [The paper by Man et. al.](Man2011.pdf) provide a good reference for you to work on this project.

<center><img src="Images/oer_volcano.png" alt="oer" style="width: 400px;"/><br>
OER Activity Volcano. (Man et.al. 2011)
</center>

The universal linear scaling between ∆G_OH and ∆G_OOH helps you to asses the theoretical over-potential using a unique descriptor (∆G_O - ∆G_OH). At standard condition,

<center><img src="Images/op_eq9.png" alt="add" style="width: 500px;"/>
</center>

Your tasks include the following:
* Calculate the OER over-potential of pure SnO2 reduced surface, determine the most favorable binding site for O.
<center><img src="Images/r-sno2-sur.png" alt="add" style="width: 400px;"/><br>
Reduced SnO2(110) surface. Available binding sites: Bridge and CUS(coordination unsaturated) Sites.
</center>

* Replace one of the surface Sn atom with other dopants of your choices. (at least 3 dopants and please discuss with me before submitting your jobs). For each dopant please consider the following two possible doping sites.
<center><img src="Images/doping_sites.png" alt="add" style="width: 400px;"/><br>
Two possible sites for doping guest metal (replacing Sn).
</center>

* Discuss whether and how dopants makes SnO2 better (or worse).

<a name='qanda'></a>
## Q and A ##
1. **What if my calculation didn't finish with one submission?**

Most of your calculations will run longer than your HW3, some of them may even exceed the time limit in your job submission script. In this case, you can copy `relax.traj` to the `.traj` you have in the `qe-opt.py` and resubmit your job. The program will read the last configuration from `relax.traj` and continue the optimization process.
