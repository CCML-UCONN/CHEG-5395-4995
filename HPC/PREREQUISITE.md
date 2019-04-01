---
mathjax: false
permalink: /HPC/PREREQUISITE/
---
* [Homepage](/CHEG-5395-4995/)
## Getting Started
* [Setting up your accounts](/CHEG-5395-4995/HPC/PREREQUISITE/)
* Hands-on intro to available HPC resource
  1. [Storrs](/CHEG-5395-4995/HPC/Storrs/)
* Tutorials
  1. [UNIX Command Lines](/CHEG-5395-4995/Tutorials/UNIX/)
  2. [Python](/CHEG-5395-4995/Tutorials/Python/)


## Logging Into the Computing Clusters

Once you account on Stampede has been activated. Follow the instructions and tests to make sure everything is set up properly and functional.

## Contents
1. [Required Installation](#installation)
2. [Getting an Account](#account)
3. [Logging On](#logging)


<a name='installation'></a>

## Installation

### Mac OSX
Download and install:

* [XQuartz](http://www.xquartz.org/)

To prevent X11 from timing out, open the terminal and type:

```bash
mkdir -p ~/.ssh
echo -e "\nHost *\n ForwardX11Timeout 1000000\n" >>~/.ssh/config
```


### Windows

Download and install:

* [PuTTY](http://www.putty.org/)
* [Xming](http://sourceforge.net/projects/xming/) (Note: disable automatic installation of PuTTY with Xming. The above installer is a newer version)

<a name='account'></a>
## Getting an Account

### HPC-Storrs
HPC facility on Storrs campus are open to all members of the UConn research community. If you haven't applied one before, you can simply [request for an account](https://hpc.uconn.edu/storrs/) by clicking "**Get an Account**". A new page will pop up to ask for your NetID and password. Your HPC-Storrs account username will be your UCONN NetID and the initial password will also be the same as your NetID password.   

<a name='logging'></a>
## Logging onto the Clusters
Follow the instructions below for your system:
### Mac OSX

Open "Applications-> Utilities -> Terminal" or "Command+Space" to search Terminal using "spotlight search"
In a terminal:

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
ssh -XC NetID@login.storrs.hpc.uconn.edu
```
____

<a name='first-time'></a>
