# Using gcc
We will be using the 'Gnu Compiler Collection' (aka 'Gnu C Compiler'), or gcc, for our C++ programs. Originally designed for C programs, it was extended to include C++ programs and is one of the most common compilers for C/C++. The command, g++ calls gcc and automatically specifies the C++ library and treats all files as C++ (instead of the default as C files).

For C/C++ programs, we will do the following steps, at the command line:

1. ```
   g++ hello.cpp -o hello
   ```
    which compiles hello.cpp and store the executable in the ouput file hello

2.  ```
    ./hello
    ```
    which runs the executable file, hello