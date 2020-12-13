Today, we will explore more about how to navigate the file system from the command line. Recall in Lab 2, at a terminal window, we had typed:
```
$ mkdir thomasH
$ cd thomasH
$ pwd
```
which created a new directory, changed the current directory to it, and shows us what directory we were in.
In addition to changing to a directory, we can also change back to its "parent" directory by typing:
```
$ cd ../
```
which says go to the parent of my current location. It's often called a relative path since your destination is relative to your current location. Typing
```
$ pwd
```
will show the current working directory. Using cd ../ and pwd, answer the following:
What is the parent of your current directory?
Change to the parent directory. What is the parent of your current directory?
How many times can your repeat this?
Which directory has no parent (i.e. "ancestor" to all the other directories?)?
This simple cd ../ gives a powerful way to navigate the directories (especially when we are working on a server without a graphical user interface or automating a process). Next lab, we will introduce absolute paths that change directories to the same place each time (independent of your current working directory).