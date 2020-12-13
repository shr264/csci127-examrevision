In Lab 3, we introduced the shell, or command line, commands to create new directories (folders) and how to list the contents of those folders (and expanded on this with relative paths in Lab 4 and absolute paths in Lab 5). In Lab 6, we wrote a simple script that prints: Hello, World. We can write scripts that take the shell commands we have learned and store them in a file to be used later.

It's a bit archaic, but we can create the file with the vi editor. It dates back to the early days of the Unix operating system. It has the advantage that it's integrated into the Unix operating system and guaranteed to be there. It is worth trying at least once (so if you're in a bind and need to edit Unix files remotely, you can), but if you hate it (which is likely), after you've tried it this once you can go back to an editor with graphical interface.

Let's create a simple shell script with vi:

1. Open a terminal window.
2. Type in the terminal window: vi setupProject
3. To add text to the file, begin by typing i (the letter i) which stands for "insert"
4. Type the lines:
   ```
    #Your name here
    #October 2017
    #Shell script:  creates directories for project
    mkdir projectFiles
    cd projectFiles
    mkdir source
    mkdir data
    mkdir results
    ```
5. Click on the ESC (escape key-- usually on the upper row of keys) which escapes from insert mode.
6. Type: :wq which stands for "write my file" and "quit" (the ":" is necessary-- it tells vi that you want to use the menu commands).
7. This brings us back to the terminal window. Type ls to see a listing of the directory, which should include the file, setupProject, you just created.
8. Next, we'll change the permissions on the file, so that we can run it directly, by just typing its name:
chmod +x setupProject
(changes the "mode" to be executable).
9. To run your shell script, you can now type its name at the terminal:
./setupProject
10. Check to see that your script works, type ls to see the new directories your script you created.

If you hate vi, just edit using gEdit in Linux, TextEdit in MacOs, notepad in Windows or IDLE.