---
mathjax: false
permalink:  /HPC/Storrs/
---

## Getting Started
*  [Getting your accounts](/CCML/HPC/PREREQUISITE/)
* Setting up accounts on HPC clusters
  1. [Storrs](/CCML/HPC/Storrs/)
  2. [TACC](/CCML/HPC/TACC/)
* Tutorials
  1. [UNIX Command Lines](/CCML/Tutorials/UNIX/)
  2. [Python](/CCML/Tutorials/Python/)

____
## Contents
1. [First Time Logging On](#first-time)
2. [Quick Tests](#testing)
3. [Batch Jobs](#batch)

### First Time Logging in ###
For the **first login** only, run the following command:

```bash
mkdir -p /scratch/$USER
ln -s /scratch/$USER $HOME/scratch
chgrp -R hpc-ccml ~/scratch
chmod g+s ~/scratch
chmod -R 750 ~/scratch
cp /home/liz18025/Group/share/bash/bashrc_copy ~/.bashrc
source ~/.bashrc
```

This will enable you to run specific software on the HCP-Storrs cluster, including the ASE interface to Quantum ESPRESSO and VASP.

There are two file partitions, the **home** and the **scratch** partition. The above lines created your directory in the **scratch** partition and a symbolic link to under your home directory pointing to your **scratch** directory. The rest of the lines set the group id to **hpc-ccml** and makes the directory only readable and executable to all group members.

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
### Batch Jobs ###
