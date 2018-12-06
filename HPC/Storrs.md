---
mathjax: false
permalink:  /HPC/Storrs/
---

## Getting Started
*  [Getting your accounts](/CCML/HPC/PREREQUISITE/)
* Hands-on of available HPC resources
  1. [Storrs](/CCML/HPC/Storrs/)
  2. [TACC](/CCML/HPC/TACC/)
* Tutorials
  1. [UNIX Command Lines](/CCML/Tutorials/UNIX/)
  2. [Python](/CCML/Tutorials/Python/)

____
# Hands-on
## Contents
1. [First Time Logging On](#first-time)
2. [Quick Tests](#testing)
3. [Batch Jobs](#batch)

<a name='first-time'></a>
### First Time Logging in ###
For the **first login** only, run the following command:

```bash
mkdir -p /scratch/$USER
ln -s /scratch/$USER $HOME/scratch
chgrp -R hpc-ccml /scratch/$USER
chmod g+s /scratch/$USER
chmod -R 750 /scratch/$USER
cp /home/liz18025/Group/share/bash/bashrc_copy ~/.bashrc
source ~/.bashrc
```

This will enable you to run specific software on the **HCP-Storrs** cluster, including the ASE interface to **VASP** and **Quantum ESPRESSO**.

There are two file systems, **home** and **scratch**. The above lines created your directory under the **scratch** partition and a symbolic link(shortcut) under your home directory pointing to your **scratch** directory. The rest of the lines set the group id to **hpc-ccml** and makes the directory only readable and executable to all group members.

<a name='testing'></a>
### Quick Tests ###
Once you are logged into the terminal, run:

```bash
ase-gui
```

and make sure a graphical interface appears. Next, run Python in interactive mode by typing:

```bash
python
```

and make sure the following commands work:

```python
import ase
import numpy
```
<a name='batching'></a>
###Job Management###
Most of our jobs require dedication of multiple nodes. Therefore jobs cannot be executed on the front node(the node everyone interfaces when logged onto the cluster). The HPC cluster use a job management system to process the resource requirements and its distribution to working/slave nodes. Some more useful information about the batch system on **HPC-Storrs** can be found [here]()

You can find several different job submission scripts in the following directory:
`$GRPDIR/share/example/scripts/batch/`

Pick the one meets your need most and edit the corresponding fields.

These instructions are specific to the **HPC-Storrs** cluster.

```bash
sbatch <script_file>
```
Submit the job defined by the script file to the queue.

____

```bash
sq
```

Check the status of your jobs. You will get something like the following:

```
JOBID PARTITION       QOS     NAME     USER ST       TIME  NODES   CPUS NODELIST(REASON)
1775578   general   general vasp.sub ******* PD       0:00      5    120 (Resources)         
```
____


Shows more useful details about the job, including the working directory of the script.
```bash
squeue -u $USER -o '%.7i %.9P %.8j %.8u %.2t %.10M %.6D %R %Z'
```
You will get something like the following:

```
JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON) WORK_DIR
1775578   general vasp.sub ******* PD       0:00      5 (Resources) /gpfs/scratchfs1/*******/projects/seed/PdO/lsf-npo/101/high-co-cov/h2_ads/neb/0t/step2/neb
```
____
To delete your job. You can get the job ID from ```sq``` and use scancel to delete it.

```bash
scancel <job_ID>
```
