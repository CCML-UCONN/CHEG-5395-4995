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

### First Time Logging in ###
For the **first login** only, run the following command:

```bash
cp /home/liz18025/Group/share/bash/bashrc_copy ~/.bashrc
source ~/.bashrc
```

This will enable you to run specific software on the HCP-Storrs cluster, including the ASE interface to Quantum ESPRESSO.

There are two file partitions, the `home` and the `scratch` partition. Go ahead and make a symbolic link to the `scratch` partition using (replace XXXXXXX with your UCONN NetID):

```bash
mkdir -p /scratch/XXXXXXX
ln -s /scratch/XXXXXXX scratch
```

## Making Sure Everything Works ##

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
