Last lab, we introduced relative paths for navigating the directories via the shell. Relative paths (e.g. cd ../) used the current location when executing. We can also use absolute paths that are independent of your location. For example,

```
$ cd /usr/bin
$ pwd
$ ls
```
will change your working directory to one of the machine's standard bin directories which is filled with programs, or binaries. The next two commands show the path to the working directory and list its contents. These binaries are in a central location to make them easier to find and use.
Since it is nice to be able to return to your default, or home directory, there is a built-in short-cut for home (~). Try
```
$ cd ~
$ pwd
$ ls
```
The first command will return you to your home directory, no matter where you started.