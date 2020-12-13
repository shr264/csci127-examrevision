# More on Unix: Using Pipes

Let's use a pipe to count the number of files from October. First, we need to take the output from ls and direct it into a program that can find patterns. A popular one on Unix is called grep (it searches for patterns, which are also called regular expressions or 're'-- the name comes from global search for regular expressions program). Let's have it look for 'Oct':
```
ls -l | grep "Oct"
```
Note that between the ls -l and the grep "Oct" is a pipe ('|') that directs the outflow from the ls command to the inflow of the grep command:

We can use the pipe to take the output of the grep command and send it to a program that counts the number of lines. This program, wc, counts characters (option -m), words (option -w), and lines (option -l). We'll use the -l option to count lines:

```
ls -l | grep "Oct" | wc -l
```