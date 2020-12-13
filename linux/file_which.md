# More Useful Unix Commands

Now that we are creating executable programs, it's often useful to figure out what kind of file is in your directory. For example, if you were not sure what type of file, hello is, you could type at the command line:

```
file hello
```
file is the name of the command, and hello is the input parameter to the command. If you would like to find out the type of several files, you could type each separately:
```
file hello hello.cpp hello.py
```
(assuming all of those files are your working directory).
Or, you could use a "wildcard" that matches all files whose names match a pattern. For example:
```
file hello*
```
will tell you all type of every file that begins with the hello followed by 0 or more other characters.
Similarly,
```
file *
```
will tell you all type of every file in your current working directory.
It's often useful to figure out which version of a program you're using (since there could be multiple ones on your computer). To do that, there's a command, which that will tell which version of the program it's using by default. For example,
```
which g++
```
will show the location of the g++ program.