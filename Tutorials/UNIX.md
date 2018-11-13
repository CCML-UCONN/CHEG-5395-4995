---
mathjax: false
permalink: /Tutorials/UNIX/
---

# Getting Started
1. [Logging Into the Computing Clusters](/CCML/HPC/PREREQUISITE/)
2. [Basic UNIX](../UNIX/)
3. [Python](../Python/)

____

## Basic UNIX

## Contents
1. [Basic Comamands](#basic-commands)
2. [Wildcards](#wildcards)
3. [Text Editors](#text-editors)
<a name='basic-commands'></a>

## Basic Commands

These are some of the basic commands that you will be using in the shell on a daily basis.

____

```bash
ase-gui <file_name>
```
Graphical user interface for the Atomic Simulation Environment (ASE). This is the tool you will be using for viewing or setting up your structures.

____

```bash
cd ..
```
Move up one directory.

____

```bash
cd <directory_name>
```
Changes directory to the one provided. If no directory is given, the default is to return you to your home directory (/home/username/)

____

```bash
cp <source_file_with_path> <destination_path>
```
Copies files or directories from the source_file_with_path to the destination_path

____

```bash
cp -r <source_file_with_path> <destination_path>
```
Copy recursively. Useful for copying multiple files and directories (copies contents of the subdirectories).

____

```bash
cp -u <source_file_with_path> <destination_path>
```
Update. Copies only if the source file is newer than the destination file or the destination file does not exist.

____

```bash
mkdir <directory_name>
```
Create new a new directory.

____

```bash
mv <source_file> <destination_file>
```
Move or rename file.

____

```bash
ls <directory_name>
```
Lists the files and directories contained within the directory. Leave blank for present directory.

____

```bash
ls -t
```
List files in chronological order.

____

```bash
ls -la
```
List all files even those starting with a dot '.' which are generally not listed.

____

```bash
ls | more
```
If the number of files in a directory is too large to fit in a single screen this command lists files and directories page after page on spacebar keystroke.

____

```bash
pwd
```
Provides the “present working directory,” i.e.   the current folder.

____

```bash
rm <file>
```
Remove files. This is always *permanent*.

____

```bash
rm -r <file_or_directory_with_path>
```
Remove file or the directory and its contents recursively.

____

```bash
rmdir <directory_name>
```
Remove an empty directory. Use rm -r to remove recursively, such as if directory contains files (be careful).

____

```bash
cat <file_name>
```
Print out contents of a text file or files within the shell.

<a name='wildcards'></a>

## Wildcards
Wildcards can be used to perform commands on multiple files simultaneously.

____

```bash
?
```

Single character. Example: ```ag neb?.traj neb??.traj``` will use ```ag``` to open all files containing one or two characters between neb and .traj

____

```bash
*
```
Any number of characters. Example: ```ls *.traj``` will list all ```.traj``` files.

<a name='text-editors'></a>

## Text Editors
There are several text editors available. Popular ones include [vim](https://www.cs.colostate.edu/helpdocs/vi.html) and [nano](https://www.nano-editor.org/dist/v2.0/nano.html).
