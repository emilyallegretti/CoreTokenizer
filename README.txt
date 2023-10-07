Core Tokenizer/Scanner Project
By Emily Allegretti

***FILES IN THIS PROJECT***

CoreTokenizerMain.py:
This is the main driver file for the project that contains the main function, which creates the Scanner object and prints out each token that
is read in from the file by Scanner. Specifically, it prints out the unique number associated with the token (1-34).

Scanner.py
This file contains the definition and methods for the Scanner class, an instance of which is responsible for tokenizing an input file using the Core DFA and 
allowing clients to access and iterate through the stored tokens. 

Token.py
This file contains the enum class definition for Core Tokens. Since every type of Core token is associated with a unique number, this file defines 
an enum and associated value for every Core token. 

***USAGE***
Prerequisites:
Python installed on your machine

To run the Core Tokenizer:
1. Download and unzip the project folder
2. From the command line, cd into unzipped project folder
3. Run this command:
    python CoreTokenizerMain.py <filename>
    where <filename> is the input file to be tokenized. This must be a .txt file, and it must be either an absolute filepath if not in 
    the current project folder, or just a filename if it is inside the project folder.  