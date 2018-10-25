---
mathjax: false
permalink: /HPC/
---

## Getting Started
* [Setting up accounts on HPC clusters.](../HPC/)
* Tutorials for [UNIX command lines](../UNIX/) and [Python](../Python/)

____

## Logging Into the Computing Clusters

Once you account on Stampede has been activated. Follow the instructions and tests to make sure everything is set up properly and functional.

## Contents
1. [Required Installation](#installation)
2. [Getting an Account](#account)
3. [Logging On](#logging)
4. [First Time Logging On](#first-time)
5. [Making Sure Everything Works](#testing)

<a name='installation'></a>

## Installation

### Mac OSX
Download and install:

* [XQuartz](http://www.xquartz.org/)

To prevent X11 from timing out, open the terminal and type:

```bash
mkdir -p ~/.ssh
echo $'\nHost *\n ForwardX11Timeout 1000000\n' >>~/.ssh/config
```


### Windows

Download and install:

* [PuTTY](http://www.putty.org/)
* [Xming](http://sourceforge.net/projects/xming/) (Note: disable automatic installation of PuTTY with Xming. The above installer is a newer version)


## Getting an Account

### HPC-Storrs
HPC facility on Storrs campus are open to all members of the UConn research community. If you haven't applied one before, you can simply [request for an account](https://hpc.uconn.edu/storrs/) by clicking "**Get an Account**". A new page will pop up to ask for your NetID and password. Your HPC-Storrs account username will be your UCONN NetID and the initial password will also be the same as your NetID password.   

### TACC-Stampede
Our TACC-Stampede allocation is managed through XSEDE funded by NSF. Please visit XSEDE user portal first to [create an account](https://portal.xsede.org/my-xsede?p_p_id=58&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view&_58_struts_action=%2Flogin%2Fcreate_account). After the submission of the account request, you will receive an approval email in 24-48 hrs. Log onto your XSEDE account and [check your TACC-Stampede account username](https://www.xsede.org/group/xup/accounts)(most probably start with **tgxxxxxx**). Remember to email or slack me your XSEDE and TACC account usernames as soon as you receive them.

Go to [TACC user portal](https://portal.tacc.utexas.edu/home) and click "**Log in with TACC ACCOUNT**", put your username ("**tgxxxxxx**) and password to login. If you don't know your password, you might want to try "**Forgot your password**". After login, You will also be asked to setup the Multi-factor Authorization.

## Logging onto the Clusters
Follow the instructions below for your system:
### Mac OSX

Open "Applications-> Utilities -> Terminal" or "Command+Space" to search Terminal using "spotlight search"
In a terminal:
```bash
ssh -X username@stampede.tacc.utexas.edu
```

```bash
ssh -X NetID@login.storrs.hpc.uconn.edu
```
### Windows
Launch Xming. You will always need to have this open in order to forward graphical windows from the external clusters.

Start PuTTY, and:

* “Session” → “Host Name” `username@stampede.tacc.utexas.edu` for **Stampede** and `NetID@login.storrs.hpc.uconn.edu` for **HPC-Storrs**
* “Connection” → “SSH” → “X11” check “Enable X11 forwarding”
* Back in “Session”, you can **save these settings for next time**.

You can start putty several times, if you need several terminal windows; only one instance of Xming needed.


### Linux ###

In a terminal:
```bash
ssh -X username@stampede.tacc.utexas.edu
```
```bash
ssh -X NetID@login.storrs.hpc.uconn.edu
```
____

<a name='first-time'></a>

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
