Let's create a new directory, or folder, to hold your images (using the shell or command line). Where it says thomasH below, replace with your name. It is easier if you avoid spaces in the names:

Open a new terminal window.
In the terminal window, type:
```
$ pwd
```
(The $ represents the prompt at the command line-- no need to type it.)
This tells you the path, or location, of your current working directory.

To see what is in the folder, you request a 'listing':
```
$ ls
```
To add a new directory, we type:
```
$ mkdir thomasH
```
(replace thomasH with your name to create a directory for you!).
Now, when we list the current directory, we should see the new item (namely the directory with your name):
```
$ ls
```
Let's change directories:

```
$ cd thomasH
```
If we ask for a listing (ls), we will now see the contents of your directory, which is initially empty.
The graphical interface and shell are operating on the same underlying system, so, changes you make with one can be seen by the other. If you use your OS' graphical user interface to open the folder (directory) you started in when you typed pwd, you will see the folder you just created.
In the next lab, we will explain how to copy and move files between directories.