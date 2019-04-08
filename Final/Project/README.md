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


<a name='oer'></a>
## SnO2-based OER Catalysts ##
Path:`/home/liz18025/shared/cheg4995-5395/final_project/OER`

Pure SnO2 itself is one of the worst OER catalysts, due to weak binging of O species on the surface. You will be calculating the adsorption free energy of O and OH on pure and doped SnO2(110) surface to obtain the theoretical OER over-potential. [The paper by Man et. al.](Man2011.pdf) provide a good reference for you to work on this project.

<center><img src="Images/oer_volcano.png" alt="oer" style="width: 400px;"/><br>
OER Activity Volcano. (Man et.al. 2011)
</center>

The universal linear scaling between ∆G_OH and ∆G_OOH helps you to asses the theoretical over-potential using a unique descriptor (∆G_O - ∆G_OH). At standard condition,

<center><img src="Images/op_eq9.png" alt="add" style="width: 300px;"/>
</center>

Your tasks include the following:

1. Calculate the OER over-potential of pure SnO2 reduced surface, determine the most favorable binding site for O.
<center><img src="Images/r-sno2-sur.png" alt="add" style="width: 400px;"/><br>
Reduced SnO2(110) surface. Available binding sites: Bridge and CUS(coordination unsaturated) Sites.
</center>
2. Replace one of the surface Sn atom with other dopants of your choices. (at least 3 dopants and please discuss with me before submitting your jobs). For each dopant please consider the following two possible doping sites.
<center><img src="Images/doping_sites.png" alt="add" style="width: 400px;"/><br>
Two possible sites for doping guest metal (replacing Sn).
</center>
3. Discuss whether and how dopants makes SnO2 better (or worse).

<a name='qanda'></a>
## Q and A ##
1. What if my calculation didn't finish with one submission?
Most of your calculations will run longer than your HW3, some of them may even exceed the time limit in your job submission. In this case, you will can copy `relax.traj` to the `.traj` you have in your `qe-opt.py` and resubmit your job. The program will read the last configuration from `relax.traj` and continue the optimization process.
