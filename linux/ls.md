The ls command has many options to give more information about what is in a folder. For example,
```
$ ls -l
```
is the "long" format of ls and gives additional information such as permissions (who is allowed to read, write, or execute the file), the owner and owner's group, the size, and the date of creation. For example, if our folder had a single directory, thomasH (like we created in Lab 2), when you type the command, you will see output similar to:
```
$ ls -l
drwxr-xr-x  2 stjohn  wheel  68 Jan  7 21:00 thomasH/
```
Two useful commands are cp and mv which copy and rename (move) files. If we have a folder with:
```
$ ls
p1.py     p2.py     programs/
```
We can make a copy of a file by using the cp and the name of the old file and the new file:
```
$ cp p2.py p3.py
```
The result would be:
```
$ ls
p1.py     p2.py     p3.py     programs/
```
Renaming a file follows the same format:
```
$ mv p1.py prog1.py
The result would be:
$ ls
p2.py     p3.py     prog1.py  programs/
```
You can also move programs into a folder by giving the directory's name as the last input to the mv command:
```
$ mv prog1.py programs
```
The result would be:
```
$ ls
p2.py     p3.py     programs/
```
If we look inside the programs folder, we see:
```
$ ls programs
prog1.py
```