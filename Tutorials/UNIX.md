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
3. [Advanced Commands](#advanced)
4. [Text Editors](#text-editors)
5. [Exercises](#exercises)


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
Remove an empty directory. Use ```rm -r``` to remove recursively, such as if directory contains files (be careful).

____

```bash
less <file_name>
```
or
```bash
more <file_name>
```
Print out contents of a text file or files within the shell.

____

```bash
grep [keyword] <file_name>
```
Search "keyword" in each File.

____
```bash
man <command>
```
This is the most powerful command on this page. It prints out the manual of the command, including options and syntax.

____

```bash
scp [options] username1@source_host:directory1/filename1 username2@destination_host:directory2/filename2
```
Securely transfer files between two Unix computers. Most of the time you are transferring files between your local computer and HPC clusters.

**from the cluster to your computer**
```bash
scp username@hostname:directory1/filename1 directory2/filename2
```

**from the cluster to your computer**
```bash
scp directory2/filename2 username@hostname:directory1/filename1
```
use  ```scp -r``` if your are transferring a directory.

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

<a name='advanced'></a>
## Advanced Commands for File Streaming
```bash
sed
```
[sed](https://www.geeksforgeeks.org/sed-command-in-unix/) command in UNIX is stands for stream editor and it can perform lot’s of function on file like, searching, find and replace, insertion or deletion.

```bash
awk
```
[awk](Awk is a scripting language used for manipulating data and generating reports) is a scripting language used for manipulating data and generating reports

```bash
 env|sed -n '/USER/p'|awk -F '=' '{print $2}'
```
The above line reads output from the command ```env```, from the output, ```sed -n '/USER/p'``` finds the line contains the keyword "USER", ```awk -F '=' '{print $2}'``` splits the line using "=" as the separator, and prints the second element.
`|` is the separator for pipelines of multiple commands, the next command takes the output of the previous command as the input.

<a name='text-editors'></a>

## Text Editors
There are several text editors available. Popular ones include [vim](https://www.cs.colostate.edu/helpdocs/vi.html) and [nano](https://www.nano-editor.org/dist/v2.0/nano.html).

<a name='exercises'></a>
## Exercises
1. Login to **HPC-Storrs**
2. Go to your **scratch** directory and create a new folder called "trail"
3. Go to the new folder "trail", and copy a file named "Numb" from "/home/liz18025/Group/share/doc/exercises" to the current directory.
4. Rename the copied file as "MyNumb"
5. Now open "MyNumb" with any text-editor: **a.** change the title(first line) from "Numb" to "Not Numb"; **b.** insert a new line after the title with your UCONN NetID; **c.** delete the last two lines of this file.
6. ```grep``` all lines that contains "numb" in the file "MyNumb"
7. Send the path of the current directory to me through Slack or Email.
