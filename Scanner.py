from Token import *

# A Scanner for the Core language that tokenizes each line of a given input file into tokens for the Core language, stored in a private data structure that '
# can be iterated through and accessed with instance methods getToken(), skipToken(), intVal(), and idName(). 
class Scanner:
    error_message = "ERROR: Invalid Token. Scanner aborted"
    # Constructor.
    def __init__(self, filename): 
        # open file and tokenize line-by-line into tokens
        with open(filename, 'r') as self.input:
            self._tokens = []
            self._tokenizeLine(self.input)
            # initialize cursor to first token index
            self._cursor = 0
            # initialize a Map that will hold the string or numerical value for identifiers and integers, respectively. 
            # the key will be the index of that integer or identifier's location in the tokens array, and the value will be its actual value. 
            self.actual_values = {}

    # Tokenizes a line from the input file into tokens array. 
    def _tokenizeLine(self): 
        line = (self.input).readline()

        # check if the line is entirely whitespace; if so, continue to read lines until one without whitespace is found
        while line.isspace():
            line = (self.input).readline()
         # check if we've reached the end of the file, append EOF token if so and return
        if line == "":
           self._tokens.append(Token.EOF)
           print("End of file reached.")
           return
        # analyze each character in the line to determine its token
        i=0
        while i < len(line):
            currChar = line[i]
        # CASES:
         # WHITESPACE
         # if whitespace character is found, continue iterating through line until next non-whitespace is found
            while currChar.isspace():
               i=i+1
               currChar=line[i]

        # INTEGERS
            if currChar.isdigit():
               # begin building string of digits now that we've come across one decimal digit--digitString will hold this string
               digitString=currChar
               #iterate through line until next character is not a digit
               i = i+1
               while (i<len(line) & line[i].isdigit()):
                  digitString=digitString+line[i]
                  i=i+1
              # check if current character is a letter (not a special character)--if so, this is an illegal token and scanner should stop reading.
               if i<len(line) & line[i].isalpha():
                  self._tokens.append(Token.INVALID)
                  print(self.error_message)
                  break
            # if we've gotten to this point, digitString is a legal string of decimal digits
            # add its numeric value to actual_values and update tokens array
               self._tokens.append(Token.NUMBER)
               self.actual_values[len(self._tokens)-1] = int(digitString)      

        # IDENTIFIERS
            elif currChar.isupper():
               # begin building identifier string now that we've come across an identifier character--idString will hold this string
               idString=currChar
               # iterate through line until next character is not an uppercase letter or digit
               i = i+1
               while (i < len(line)) & (line[i].isdigit() | line[i].isupper()):
                  idString = idString+line[i]
                  i = i+1
               # check if current character is a lowercase letter (not a special character)--if so, this is an illegal token and scanner should stop reading.
               if i < len(line) & line[i].islower():
                  self._tokens.append(Token.INVALID)
                  print(self.error_message)
                  break
               # if we've gotten to this point, idString is a legal identifier
               # add its string value to actual_values and update tokens array
               self._tokens.append(Token.ID)
               self.actual_values[len(self._tokens) - 1] = idString

        # SPECIAL CHARACTERS
            elif currChar==";":
               self._tokens.append(Token.SEMICOLON)
               i=i+1

            elif currChar==",":
               self._tokens.append(Token.COMMA)
               i=i+1

            elif currChar == "[":
               self._tokens.append(Token.OPEN_BRACKET)
               i=i+1

            elif currChar=="]":
               self._tokens.append(Token.CLOSE_BRACKET)
               i=i+1

            elif currChar=="(":
               self._tokens.append(Token.OPEN_PAREN)
               i=i+1


            elif currChar==")":
               self._tokens.append(Token.CLOSE_PAREN)
               i=i+1

            elif currChar == "+":
               self._tokens.append(Token.PLUS)
               i=i+1

            elif currChar == "-":
               self._tokens.append(Token.MINUS)
               i=i+1

            elif currChar == "*":
               self._tokens.append(Token.ASTERISK)
               i = i+1

            elif currChar=="&":
               # check to see if next character is also an ampersand; if not, this token is illegal
               i=i+1
               if (i<len(line) & line[i] == "&"):
                  self._tokens.append(Token.AND)
               else:
                  self._tokens.append(Token.INVALID)
                  print(self.error_message)
                  break
               
            elif currChar == "|":
               # check to see if next character is also a vertical bar; if not, this token is illegal
               i = i+1
               if (i < len(line) & line[i] == "|"):
                  self._tokens.append(Token.OR)
               else:
                  self._tokens.append(Token.INVALID)
                  print(self.error_message)
                  break
               
            elif currChar == "!":
               # check to see if next character is an equals sign for 'greedy tokenizing'
               i = i+1
               if (i < len(line) & line[i] == "="):
                  self._tokens.append(Token.NOT_EQUALS)
               else: # otherwise just add not symbol
                  self._tokens.append(Token.NOT)

            elif currChar == ">":
               # check to see if next character is an equals sign for 'greedy tokenizing'
               i = i+1
               if (i < len(line) & line[i] == "="):
                  self._tokens.append(Token.GT_EQUALS)
               else: #otherwise just add GT symbol
                  self._tokens.append(Token.GREATER_THAN)

            elif currChar == "<":
               # check to see if next character is an equals sign for 'greedy tokenizing'
               i = i+1
               if (i < len(line) & line[i] == "="):
                  self._tokens.append(Token.LT_EQUALS)
               else: #otherwise just add LT symbol
                  self._tokens.append(Token.LESS_THAN)

            elif currChar == "=":
               # check to see if next character is an equals sign for 'greedy tokenizing'
               i = i+1
               if (i < len(line) & line[i] == "="):
                  self._tokens.append(Token.EQUALS)
               else: #otherwise just add single equals symbol
                  self._tokens.append(Token.ASSIGN)

        # RESERVED WORDS
            # program
            elif currChar == "p":
               # check to see if rest of characters make up 'program', otherwise we have an illegal token
               substring='rogram'
               for letter in substring:
                  i=i+1
                  if i==len(line) | line[i] != letter:
                     print(self.error_message)
                     self._tokens.append(Token.INVALID)
                     break
                  else:
                     i=i+1
                # break out of outer loop if 'program' wasn't found, otherwise add program token to array
               if self._tokens[-1]==Token.INVALID:
                  break
               else: 
                  self._tokens.append(Token.PROGRAM)

             # begin
            elif currChar == "b":
               # check to see if rest of characters make up 'begin', otherwise we have an illegal token
               i=i+1
               substring='egin'
               for letter in substring:
                  if i==len(line) | line[i] != letter:
                     print(self.error_message)
                     self._tokens.append(Token.INVALID)
                     break
                  else:
                     i=i+1
                # break out of outer loop if 'begin' wasn't found, otherwise add begin token to array
               if self._tokens[-1]==Token.INVALID:
                  break
               else: 
                  self._tokens.append(Token.BEGIN)

             # then
            elif currChar == "t":
               # check to see if rest of characters make up 'then', otherwise we have an illegal token
               i=i+1
               substring='hen'
               for letter in substring:
                  if i==len(line) | line[i] != letter:
                     print(self.error_message)
                     self._tokens.append(Token.INVALID)
                     break
                  else:
                     i=i+1
                # break out of outer loop if 'then' wasn't found, otherwise add then token to array
               if self._tokens[-1]==Token.INVALID:
                  break
               else: 
                  self._tokens.append(Token.THEN)

             # loop
            elif currChar == "l":
               # check to see if rest of characters make up 'loop', otherwise we have an illegal token
               i=i+1
               substring='oop'
               for letter in substring:
                  if i==len(line) | line[i] != letter:
                     print(self.error_message)
                     self._tokens.append(Token.INVALID)
                     break
                  else:
                     i=i+1
                # break out of outer loop if 'loop' wasn't found, otherwise add loop token to array
               if self._tokens[-1]==Token.INVALID:
                  break
               else: 
                  self._tokens.append(Token.LOOP)

             # read
            elif currChar == "r":
               # check to see if rest of characters make up 'read', otherwise we have an illegal token
               i=i+1
               substring='ead'
               for letter in substring:
                  if i==len(line) | line[i] != letter:
                     print(self.error_message)
                     self._tokens.append(Token.INVALID)
                     break
                  else:
                     i=i+1
                # break out of outer loop if 'read' wasn't found, otherwise add read token to array
               if self._tokens[-1]==Token.INVALID:
                  break
               else: 
                  self._tokens.append(Token.READ)

            # write, while 
            elif currChar == "w":
               # if next char is 'h', test to see if we have while keyword.
               # if next char is 'r', test to see if we have write keyword.
               # otherwise, we have an illegal token.
               i=i+1
               if i< len(line) & line[i]=="h":
                  substring="hile"
                  for letter in substring:
                    if i == len(line) | line[i] != letter:
                        print(self.error_message)
                        self._tokens.append(Token.INVALID)
                        break
                    else: 
                       i=i+1
                # break out of outer loop if 'while' wasn't found, otherwise add while token to array
                  if self._tokens[-1] == Token.INVALID:
                     break
                  else:
                     self._tokens.append(Token.WHILE)
               elif i<len(line) & line[i]=="r":
                  substring = "rite"
                  for letter in substring:
                    if i == len(line) | line[i] != letter:
                        print(self.error_message)
                        self._tokens.append(Token.INVALID)
                        break
                    else:
                       i = i+1
                  # break out of outer loop if 'write' wasn't found, otherwise add write token to array
                  if self._tokens[-1] == Token.INVALID:
                     break
                  else:
                     self._tokens.append(Token.WRITE)
               else:
                  print(self._error)
                  self._tokens.append(Token.INVALID)
                  break

            # int, if
            elif currChar == "i":
               # if next char is 'n', test to see if we have int keyword.
               # if next char is 'f', we have an if keyword.
               # otherwise, we have an illegal token.
               i = i+1
               if i<len(line) & line[i] == "n":
                  i=i+1
                  if i<len(line) & line[i] == "t":
                    self._tokens.append(Token.INT)
                    i=i+1
                  else:
                    print(self._error)
                    self._tokens.append(Token.INVALID)
                    break
               elif i<len(line) & line[i] == "f":
                  self._tokens.append(Token.IF)
                  i=i+1
               else:
                  print(self._error)
                  self._tokens.append(Token.INVALID)
                  break

            # else, end
            elif currChar == "e":
               # if next char is 'l', test to see if we have else keyword.
               # if next char is 'n', test to see if we have end keyword.
               # otherwise, we have an illegal token.
               i = i+1
               if i<len(line) & line[i] == "l":
                   substring = "lse"
                   for letter in substring:
                    if i == len(line) | line[i] != letter:
                        print(self.error_message)
                        self._tokens.append(Token.INVALID)
                        break
                    else:
                       i = i+1
                  # break out of outer loop if 'else' wasn't found, otherwise add else token to array
                   if self._tokens[-1] == Token.INVALID:
                     break
                   else:
                     self._tokens.append(Token.ELSE)

               elif i<len(line) & line[i] == "n":
                  i=i+1
                  if i < len(line) & line[i] == "d":
                    self._tokens.append(Token.END)
                    i = i+1
                  else:
                    print(self._error)
                    self._tokens.append(Token.INVALID)
                    break

               else:
                  print(self._error)
                  self._tokens.append(Token.INVALID)
                  break


               
                     

               
                
               
         
    # Moves cursor to next token in tokens array, unless the current token being pointed at
    # by cursor is 33 (EOF) or 34 (illegal token), in which the cursor is not moved. 
    # If advancing the cursor forward puts it past the last index of the tokens array, the next line from the file is 
    # tokenized into tokens array with tokenizeLine(). 
    def _skipToken(self):
       if self.getToken() < 33:
        self._cursor=self.cursor+1
        if self._cursor == len(self._tokens):
         self._tokenizeLine(self)

    # Returns the token number that is being pointed to in tokens array by cursor.
    def getToken(self):
       return self._tokens[self._cursor]

    def intVal(self):
       return
    def idName(self):
       return