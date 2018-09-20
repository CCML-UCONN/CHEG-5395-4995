---
layout: page
mathjax: true
permalink: /Project/
---

## Course Project ##
1. [Introduction](#intro)
2. [Deadlines](#deadlines)
3. [Calculations](#calcs)
4. [Analysis](#analysis)
5. [Final Report](#report)


For the Final Project, you will be studying thermo-chemical ammonia synthesis on 2D MXenes (M<sub>2</sub>X) with X = C or N. Each student will be assigned a MXene to work on either a carbide or a nitride (see list of Assigned Projects). The students will work in groups of two on the same MXene to perform calculations individually, however, complementing each other. Each pair of students will present their results in class that will be critiqued by another group of two. Finally, these four students will jointly write a final report on the combined data. The due date for the final written report is <font color="red">5/1 at 5:00 PM (hard deadline)</font>.

Please make use of the [Piazza](https://piazza.com/) page for troubleshooting, discussions and for sharing results.

Turn in your final report by emailing a PDF file to:

```
alevoj@seas.upenn.edu, liangzha@seas.upenn.edu
```

<a name='intro'></a>

## Introduction ##

The thermo-chemical synthesis of ammonia is accomplished through the [Haber-Bosch process](http://en.wikipedia.org/wiki/Haber_process), where nitrogen gas reacts with hydrogen gas via:

$$
\mathrm{N_2+3H_2\rightarrow 2NH_3}
$$

This process is crucial for the industrial production of fertilizers and chemical feedstocks. Typically, an iron catalyst is used to stabilize the bond-breaking of the N<sub>2</sub> species. The reaction can be separated into elementary reaction steps ([Honkala et. al. (2005)](http://dx.doi.org/10.1126/science.1106435) for more details):

$$
\begin{align}
\mathrm{N_{2\,(g)}} &\rightarrow \mathrm{2N*}\\
\mathrm{H_{2\,(g)}} &\rightarrow \mathrm{2H*}\\
\mathrm{N* + H*} &\rightarrow \mathrm{NH*}\\
\mathrm{NH* + H*} &\rightarrow \mathrm{NH_2*}\\
\mathrm{NH_2* + H*} &\rightarrow \mathrm{NH_3*}\\
\mathrm{NH_3*} &\rightarrow \mathrm{NH_{3\,(g)}}
\end{align}
$$

A free energy diagram is illustrated below:

<center><img src="../Images/N2_path.jpg" alt="N2 path" style="width: 450px;"/>
<br>Ammonia synthesis pathway on a Ru catalyst (<a href="http://dx.doi.org/10.1126/science.1106435">Honkala et. al. (2005)</a>)</center>

Due to the high operating pressures and temperatures required for this reaction, alternative catalysts are still needed for this process. [Medford et. al. (2015)](http://dx.doi.org/10.1016/j.jcat.2014.12.033) have suggested that the linear scaling between the dissociation energy of N<sub>2</sub> and its transition state energy prevents most catalysts from achieving a high rate. Assuming that the bond-breaking of N<sub>2</sub> is rate limiting, then traditional metal catalysts have a transition state that is too high in energy. This is illustrated in the filled contour plot below, where the turnover frequency is plotted as a function of the transition state energy of the first N<sub>2</sub> bond breaking (*E*<sub>N-N</sub>) and the dissociation energy (∆*E*<sub>diss</sub>). A catalyst would need to behave differently from these extended surfaces in order to land in a more active region of the map. 

<center><img src="../Images/N2_volcano.png" alt="N2 volcano" style="width: 400px;"/>
<br>Filled contour plot for the turnover frequencies (Singh et. al. (2016))</center>

We will be exploring 2D MXenes where such configurations might be found. 

Your goals for the project will be to: 
(1) explore this reaction to find unique adsorption configurations and possibly more favorable thermodynamics,
(2) explore if the theormodynamics can be changed with functionalization of the MXenes,
(3) explore relations between the reaction intermediates in the pathway,
(4) compare the chemsitry of the carbide and nitride MXenes.

<a name='deadlines'></a>

## Deadlines ##
1. Show energy diagram for bare MXene on Wed April 12 on a Power Point slide (Each group)
2. Presentation date Fri Apr 21 (Each group 15 min including presentation and Q&A. Note: Total 90 mins)
3. Hand in a final written report: Mon 1 May at 5:00 PM

<a name='calcs'></a>

## Calculations ##

For the Final Project, create a `FinalProj_M2X` folder (M2X is the material you are assigned, please check [Assignment](https://cbe544.github.io/Project_Assignments/)) in your `CBE544` directory. For example, if you are assignemnt with Mo2C, please run the following command to create the directories: 

```bash
cdw
cd CBE544
mkdir FinalProj_Mo2C 
```
Please change Mo2C in the above command to the one you are assgined. 

You may run the exercises in any directory (as long as it is under `$WORK`), but keep all the final files for the project organized.

To describe the full reaction on your catalytic system, you will need to calculate the adsorption energies of all intermediates, in their most stable configuration (N\*, NH\*, NH<sub>2</sub>\*, NH<sub>3</sub>\*, H\*). A mean field approximation can be used in the analysis (*e.g.* ∆*E*<sub>2NH</sub> = 2∆*E*<sub>NH</sub>). You are not required to calculate any of the transition states for this assignment. Instead use the universal BEP relations for N<sub>2</sub> dissociation.

First, download and unarchive the files you need via:

```bash
wget https://github.com/CBE544/CBE544.github.io/raw/master/Final_Project.tar.gz
tar -zxvf Final_Project.tar.gz
```

This will create a directory named `Class`. Within, you will find pre-relaxed .traj files for the project. Your team will need the bare, O-terminated, and H-terminated MXenes. They are labeled as M2X.traj for the bare, M2XO2.traj for the O-terminated, and M2XH2.traj for the H-terminated; e.g. for Mo<sub>2</sub>C, the .traj file is Mo2C.traj for the bare MXene, Mo2CO2.traj for the O-terminated, and Mo2CH2.traj for the H-terminated.

In summary:

1. Structural relaxations on both the bare MXene and the two functionalized MXenes; that is, O-terminated and H-terminated. 
2. Adsorption energies for the intermediates in the adsorbed state (N\*, NH\*, NH<sub>2</sub>\*, NH<sub>3</sub>\*, H\*). Check all possible sites in order to determine optimal adsorption configurations. 
3. Energy diagrams for the overall reaction.
<!--4. Calculation of the reaction rate and also a free energy diagram with some temperature and pressure dependence. [Project Part 3](../ASE/Transition_States)-->

**IMPORTANT:**

When you have finished all your calculations. Confirm that your results are organized in the following way:

```bash
$WORK/CBE544/FinalProj_M2X/bare/
$WORK/CBE544/FinalProj_M2X/bare/cleansur/
$WORK/CBE544/FinalProj_M2X/bare/Adsorption/
$WORK/CBE544/FinalProj_M2X/bare/Adsorption/N/
$WORK/CBE544/FinalProj_M2X/bare/Adsorption/N/config
$WORK/CBE544/FinalProj_M2X/bare/Adsorption/NH/
$WORK/CBE544/FinalProj_M2X/bare/Adsorption/NH/config
...
$WORK/CBE544/FinalProj_M2X/O-term/
$WORK/CBE544/FinalProj_M2X/O-term/cleansur/
$WORK/CBE544/FinalProj_M2X/O-term/Adsorption/
$WORK/CBE544/FinalProj_M2X/O-term/Adsorption/N/
$WORK/CBE544/FinalProj_M2X/O-term/Adsorption/N/config
$WORK/CBE544/FinalProj_M2X/O-term/Adsorption/NH/
$WORK/CBE544/FinalProj_M2X/O-term/Adsorption/NH/config
...
$WORK/CBE544/FinalProj_M2X/H-term/
$WORK/CBE544/FinalProj_M2X/H-term/cleansur/
$WORK/CBE544/FinalProj_M2X/H-term/Adsorption/
$WORK/CBE544/FinalProj_M2X/H-term/Adsorption/N/
$WORK/CBE544/FinalProj_M2X/H-term/Adsorption/N/config
$WORK/CBE544/FinalProj_M2X/H-term/Adsorption/NH/
$WORK/CBE544/FinalProj_M2X/H-term/Adsorption/NH/config
...
```

You should rename `config` to describe the binding configuration, such as `fcc`, `hcc`, `top`, `bridge` sites. You should have one calculation per directory.

**Access Your Teammate's directory:**

The following path contains the paths to your teammate's directory, 
```bash
/home1/03672/tg829713/lnk_CBE544
```

You can create a link of the above path so that you can easily access it in the future. Be sure to change M2X to the material you are assigned

```bash
ln -s /home1/03672/tg829713/lnk_CBE544/M2X FPteam
```

<a name='analysis'></a>

## Analysis ##
Your analysis abd final report should include the following:

1. Structures of bare MXenes and the H- and O-terminated MXenes.
2. Adsorption energies and structures for all intermediates in the adsorbed state (N\*, NH\*, NH<sub>2</sub>\*, NH<sub>3</sub>\*, H\*) on the bare and the two functionalized Mxenes. Determine what is the optimal reaction site for each system. Discussion of the optimal binding configurations on the surface.
3. Energy diagrams for the overall reaction for bare, O- and H-terminated Mxenes. Preferably combined in one figure for easy comparison. Comparison between the different systems.
4. Establish scaling relations between intermediates.
5. Calculate the reaction rate of the systems you've studied with using the following assumptions:

    a. Single active site model
    
    b. N<sub>2</sub> dissociation is rate determining step
    
    c. TS of N<sub>2</sub> dissociation follows the universal BEP relation (see Eqs. on page 93 in "Fundamental Concepts in Heterogenous Catalysis" by Nørskov et al.) for either close-packed or stepped surfaces. Please motivate your choice(s) for the different systems.

    d. Use the following total energies for N2, H2, and NH3:
    ```
        N2:  -555.10 eV
        H2: -32.94 eV 
        NH3: -327.72 eV
    ```
    e. The ZPE corrections should be assumed to be negligable
    
    d. Entropies of gas phase molecules should be taken as the experimental values from [NIST](http://webbook.nist.gov/cgi/cbook.cgi?ID=C7727379&Mask=1). Please keep in mind that entropy is a function of temperature. 

<a name='report'></a>

## Final Report ##

The final report should be in the form of a 3-5 pages long mini paper including figures and tables. One report for each group of 4 people formed according to the metal of the Mxene. Please be succinct and organize it in the following way:

* Introduction (brief) - don't write too much
* Calculation details
* Results and discussion
* Conclusion (brief)

**Archieve Calculations:**

Under your final project directory, please create a folder named `opt-sites`, and then put everything there in an organized way: For each stable sites, please create a folder `X-Y-Z`, and put corresponding `.traj` and `ll_out` (use the last one if you have multiple runs) in the folder. 

* X is termination: `bare`, `H`, `O`
* Y is adsorbate: `H`, `N`, `NH`, `NH2`, `NH3`
* Z is adsorption site of the final geometry: `hcp`, `top`, `fcc`



<!--



You are welcome to share data amongst your peers to discuss broader trends. 

**If you need the energy of the fixed clusters, they are available [here](../Fixed_Lattice_Clusters/energies.txt).**

<a name='grading'></a>

## Grading ##

* 30% exercises
* 20% write-up
* 20% kinetics
* 30% calculations

<a name='reqs'></a>

## Requirements ##

At a minimum you should accomplish the following:

1. Complete the [three exercises](../ASE/).
2. Setup a M<sub>13</sub> cluster and a (111) surface and calculate adsorption energies for all intermediates.
3. Calculate transition states for the first step N<sub>2</sub> dissociation) using the fixed bond-length method. Extra credit for calculating the hydrogenation barriers.
4. Vibrational frequency and free energy calculations (initial, transition, and final states, and all adsorbed intermediates). 
5. Analysis
    1. Optimal adsorption sites (relation to transition states)
    2. Kinetic rate analysis
6. Report (3~5 pages maximum)

-->
