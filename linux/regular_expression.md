Often it's useful to find strings that match a pattern instead of spelling out the exact names of things. For example, if you wanted to know all the Python programs in your directory that are .py files, you could list out all the files and then look through visually to find them:
```
$ ls
```
But an easier way would be to specify that only the files that end in .py be printed. To do that, you can use the "wildcard" or * operator that:
```
$ ls *.py
```
The *.py says match any file that starts with any number (including 0) of characters and ends with .py.
You can use the wildcard operator in multiple places. For example, if your directory contained:
```
$ ls -l
-rw-r--r--@ 1 stjohn  staff      5308 Mar 21 14:38 quizzes.html
-rw-r--r--  1 stjohn  staff     54013 Apr 20 18:57 zoneDist.csv
-rw-r--r--@ 1 stjohn  staff      1519 Apr 22 15:14 zoneMap.py
-rw-r--r--  1 stjohn  staff  16455174 Mar 20 19:02 zoning2.html
-rw-r--r--  1 stjohn  staff  17343896 Mar 20 18:58 zoningIDS.json
```
Then the following command:
```
$ ls z*
```
prints all files that start with z and are followed by any number of characters.
Similarly,
```
$ ls *zz*
```
would all files that start with any number of characters, followed by zz, and end with any number of characters. The only file that contains this "pattern" of zz is quizzes.html.
