import sys
from Token import *

# A Scanner for the Core language that tokenizes each line of a given input file into tokens for the Core language, stored in a private data structure that '
# can be iterated through and accessed with instance methods getToken(), skipToken(), intVal(), and idName(). 
class Scanner:
    # Constructor.
    def __init__(self, filename): 
        # open file and tokenize line-by-line into tokens.
        # if file is not found, gracefully exit
        try: 
            self.input = open(filename, 'r')
        except FileNotFoundError as e:
           print(f"{e}.\nAborting program...")
           exit(1)
        self._tokens = []
        # initialize cursor to first token index
        self._cursor = 0
        # initialize a Map that will hold the string or numerical value for identifiers and integers, respectively. 
        # the key will be the index of that integer or identifier's location in the tokens array, and the value will be its actual value. 
        self.actual_values = {}
        # tokenize first line
        self._tokenizeLine()

    # Tokenizes a line from the input file into tokens array. 
    def _tokenizeLine(self): 
        line = (self.input).readline()

        # check if the line is entirely whitespace; if so, continue to read lines until one without whitespace is found
        while line.isspace():
            line = (self.input).readline()
         # ch  eck if we've reached the end of the file, append EOF token if so and return
        if line == "":
           self._tokens.append(Token.EOF)
           self.input.close()   # close file
           return
        # analyze each character in the line to determine its token
        i=0
        while i < len(line):
            currChar = line[i]

        # CASES:
         # WHITESPACE
         # if whitespace character is found, continue iterating through line until next non-whitespace is found
            if currChar.isspace():
               i=i+1
        # INTEGERS
            elif currChar.isdigit():
               # begin building string of digits now that we've come across one decimal digit--digitString will hold this string
               digitString=currChar
               #iterate through line until next character is not a digit
               i = i+1
               while (i<len(line) and line[i].isdigit()):
                  digitString=digitString+line[i]
                  i=i+1
              # check if current character is a letter (not a special character)--if so, this is an illegal token and scanner should stop reading.
               if i<len(line) and line[i].isalpha():
                  self._tokens.append(Token.INVALID)
                  break
            # if we've gotten to this point, digitString is a legal string of decimal digits
            # add its numeric value to actual_values and update tokens array
               self._tokens.append(Token.NUMBER)
               self.actual_values[len(self._tokens)-1] = digitString    

        # IDENTIFIERS
            elif currChar.isupper():
               # begin building identifier string now that we've come across an identifier character--idString will hold this string
               idString=currChar
               # iterate through line until next character is not an uppercase letter or digit
               i = i+1
               while (i < len(line)) and (line[i].isdigit() or line[i].isupper()):
                  idString = idString+line[i]
                  i = i+1
               # check if current character is a lowercase letter (not a special character or whitespace)--if so, this is an illegal token and scanner should stop reading.
               if i < len(line) and line[i].islower():
                  self._tokens.append(Token.INVALID)
                  break
               # if we've gotten to this point, idString is a legal identifier
               # add its string value to actual_values and update tokens array
               self._tokens.append(Token.ID)
               self.actual_values[len(self._tokens) - 1] = idString

        # SPECIAL CHARACTERS
        # for each special character found, add its token to tokens array
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
               if (i<len(line) and line[i] == "&"):
                  self._tokens.append(Token.AND)
                  i=i+1
               else:
                  self._tokens.append(Token.INVALID)  
                  break
               
            elif currChar == "|":
               # check to see if next character is also a vertical bar; if not, this token is illegal
               i = i+1
               if (i < len(line) and line[i] == "|"):
                  self._tokens.append(Token.OR)
                  i=i+1
               else:
                  self._tokens.append(Token.INVALID)
                  break
               
            elif currChar == "!":
               # check to see if next character is an equals sign for 'greedy tokenizing'
               i = i+1
               if (i < len(line) and line[i] == "="):
                  self._tokens.append(Token.NOT_EQUALS)
                  i=i+1
               else: # otherwise just add not symbol
                  self._tokens.append(Token.NOT)

            elif currChar == ">":
               # check to see if next character is an equals sign for 'greedy tokenizing'
               i = i+1
               if (i < len(line) and line[i] == "="):
                  self._tokens.append(Token.GT_EQUALS)
                  i=i+1
               else: #otherwise just add GT symbol
                  self._tokens.append(Token.GREATER_THAN)

            elif currChar == "<":
               # check to see if next character is an equals sign for 'greedy tokenizing'
               i = i+1
               if (i < len(line) and line[i] == "="):
                  self._tokens.append(Token.LT_EQUALS)
                  i=i+1
               else: #otherwise just add LT symbol
                  self._tokens.append(Token.LESS_THAN)

            elif currChar == "=":
               # check to see if next character is an equals sign for 'greedy tokenizing'
               i = i+1
               if (i < len(line) and line[i] == "="):
                  self._tokens.append(Token.EQUALS)
                  i=i+1
               else: #otherwise just add single equals symbol
                  self._tokens.append(Token.ASSIGN)

        # RESERVED WORDS
            # program
            elif currChar == "p":
               # check to see if rest of characters make up 'program', otherwise we have an illegal token
               # there also must be a whitespace after the end of the word, otherwise this is an illegal token
               substring='rogram'
               i=i+1
               for letter in substring:
                  if (i==len(line)) or (line[i] != letter):
                     self._tokens.append(Token.INVALID)
                     break
                  else:
                     i=i+1
                # break out of outer loop if 'program' wasn't found, otherwise add program token to array
               if (len(self._tokens) > 0) and (self._tokens[-1]==Token.INVALID):
                  break
               # make sure next token is either a whitespace or end of line, otherwise token is invalid
               else: 
                  if i == len(line) or not (line[i].isalnum()):
                    self._tokens.append(Token.PROGRAM)
                  else:
                    self._tokens.append(Token.INVALID)
                    break

             # begin
            elif currChar == "b":
               # check to see if rest of characters make up 'begin', otherwise we have an illegal token
                # there also must be a whitespace after the end of the word, otherwise this is an illegal token
               i=i+1
               substring='egin'
               for letter in substring:
                  if i==len(line) or line[i] != letter:
                     self._tokens.append(Token.INVALID)
                     break
                  else:
                     i=i+1
                # break out of outer loop if 'begin' wasn't found, otherwise add begin token to array
               if len(self._tokens) > 0 and self._tokens[-1]==Token.INVALID:
                  break
               # make sure next token is either a whitespace or end of line, otherwise token is invalid
               else:
                  if i == len(line) or not (line[i].isalnum()):
                    self._tokens.append(Token.BEGIN)
                  else:
                    self._tokens.append(Token.INVALID)
                    break

             # then
            elif currChar == "t":
               # check to see if rest of characters make up 'then', otherwise we have an illegal token
                # there also must be a whitespace after the end of the word, otherwise this is an illegal token
               i=i+1
               substring='hen'
               for letter in substring:
                  if i==len(line) or line[i] != letter:
                     
                     self._tokens.append(Token.INVALID)
                     break
                  else:
                     i=i+1
                # break out of outer loop if 'then' wasn't found, otherwise add then token to array
               if len(self._tokens) > 0 and self._tokens[-1]==Token.INVALID:
                  break
               # make sure next token is either a whitespace or end of line, otherwise token is invalid
               else:
                  if i == len(line) or not (line[i].isalnum()):
                    self._tokens.append(Token.THEN)
                  else:
                    self._tokens.append(Token.INVALID)
                    break

             # loop
            elif currChar == "l":
               # check to see if rest of characters make up 'loop', otherwise we have an illegal token
                # there also must be a whitespace after the end of the word, otherwise this is an illegal token
               i=i+1
               substring='oop'
               for letter in substring:
                  if i==len(line) or line[i] != letter:
                     self._tokens.append(Token.INVALID)
                     break
                  else:
                     i=i+1
                # break out of outer loop if 'loop' wasn't found, otherwise add loop token to array
               if len(self._tokens) > 0 and self._tokens[-1]==Token.INVALID:
                  break
               # make sure next token is either a whitespace or end of line, otherwise token is invalid
               else:
                  if i == len(line) or not (line[i].isalnum()):
                    self._tokens.append(Token.LOOP)
                  else:
                    self._tokens.append(Token.INVALID)
                    break

             # read
            elif currChar == "r":
               # check to see if rest of characters make up 'read', otherwise we have an illegal token
                # there also must be a whitespace after the end of the word, otherwise this is an illegal token
               i=i+1
               substring='ead'
               for letter in substring:
                  if i==len(line) or line[i] != letter:
                     
                     self._tokens.append(Token.INVALID)
                     break
                  else:
                     i=i+1
                # break out of outer loop if 'read' wasn't found, otherwise add read token to array
               if len(self._tokens) > 0 and self._tokens[-1] == Token.INVALID:
                  break
               # make sure next token is either a whitespace,special character or end of line, otherwise token is invalid
               else:
                  if i == len(line) or not(line[i].isalnum()):
                    self._tokens.append(Token.READ)
                  else:
                    self._tokens.append(Token.INVALID)
                    break

            # write, while 
            elif currChar == "w":
               # if next char is 'h', test to see if we have while keyword.
               # if next char is 'r', test to see if we have write keyword.
               # otherwise, we have an illegal token.
               i=i+1
               if i< len(line) and line[i]=="h":
                  substring="hile"
                  for letter in substring:
                    if i == len(line) or line[i] != letter:
                        self._tokens.append(Token.INVALID)
                        break
                    else: 
                       i=i+1
                # break out of outer loop if 'while' wasn't found, otherwise add while token to array
                  if len(self._tokens) > 0 and self._tokens[-1] == Token.INVALID:
                     break
                  # make sure next token is either a whitespace or end of line, otherwise token is invalid
                  else:
                    if i == len(line) or not (line[i].isalnum()):
                        self._tokens.append(Token.WHILE)
                    else:
                        self._tokens.append(Token.INVALID)
                        break
               elif i<len(line) and line[i]=="r":
                  substring = "rite"
                  for letter in substring:
                    if i == len(line) or line[i] != letter:
                        self._tokens.append(Token.INVALID)
                        break
                    else:
                       i = i+1
                  # break out of outer loop if 'write' wasn't found, otherwise add write token to array
                  if len(self._tokens) > 0 and self._tokens[-1] == Token.INVALID:
                     break
                  # make sure next token is either a whitespace or end of line, otherwise token is invalid
                  else:
                    if i == len(line) or not (line[i].isalnum()):
                        self._tokens.append(Token.WRITE)
                    else:
                        self._tokens.append(Token.INVALID)
                        break
               else:
                  self._tokens.append(Token.INVALID)
                  break

            # int, if
            elif currChar == "i":
               # if next char is 'n', test to see if we have int keyword.
               # if next char is 'f', we have an if keyword.
               # otherwise, we have an illegal token.
               i = i+1
               if i<len(line) and line[i] == "n":
                  substring = "nt"
                  for letter in substring:
                    if i == len(line) or line[i] != letter:
                        self._tokens.append(Token.INVALID)
                        break
                    else:
                       i = i+1
                  # break out of outer loop if 'int' wasn't found, otherwise add int token to array
                  if len(self._tokens) > 0 and self._tokens[-1] == Token.INVALID:
                     break
                  # make sure next token is either a whitespace or end of line, otherwise token is invalid
                  else:
                    if i == len(line) or not (line[i].isalnum()):
                        self._tokens.append(Token.INT)
                    else:
                        self._tokens.append(Token.INVALID)
                        break

               elif i<len(line) and line[i] == "f":
                  substring = "f"
                  for letter in substring:
                    if i == len(line) or line[i] != letter:
                        self._tokens.append(Token.INVALID)
                        break
                    else:
                       i = i+1
                  # break out of outer loop if 'if' wasn't found, otherwise add if token to array
                  if len(self._tokens) > 0 and self._tokens[-1] == Token.INVALID:
                     break
                  # make sure next token is either a whitespace or end of line, otherwise token is invalid
                  else:
                    if i == len(line) or not (line[i].isalnum()):
                        self._tokens.append(Token.IF)
                    else:
                        self._tokens.append(Token.INVALID)
                        break
               else:
                  self._tokens.append(Token.INVALID)
                  break

            # else, end
            elif currChar == "e":
               # if next char is 'l', test to see if we have else keyword.
               # if next char is 'n', test to see if we have end keyword.
               # otherwise, we have an illegal token.
               i = i+1
               if i<len(line) and line[i] == "l":
                   substring = "lse"
                   for letter in substring:
                    if i == len(line) or line[i] != letter:
                        self._tokens.append(Token.INVALID)
                        break
                    else:
                       i = i+1
                  # break out of outer loop if 'else' wasn't found, otherwise add else token to array
                   if (len(self._tokens) > 0) and self._tokens[-1] == Token.INVALID:
                     break
                   # make sure next token is either a whitespace or end of line, otherwise token is invalid
                   else:
                    if i == len(line) or not (line[i].isalnum()):
                        self._tokens.append(Token.ELSE)
                    else:
                        self._tokens.append(Token.INVALID)
                        break

               elif i<len(line) and line[i] == "n":
                  substring = "nd"
                  for letter in substring:
                    if i == len(line) or line[i] != letter:
                        self._tokens.append(Token.INVALID)
                        break
                    else:
                       i = i+1
                  # break out of outer loop if 'end' wasn't found, otherwise add end token to array
                  if (len(self._tokens) > 0) and self._tokens[-1] == Token.INVALID:
                    break
                  # make sure next token after keyword is either a whitespace or the end of the line, otherwise the token is invalid
                  else:
                    if i == len(line) or not(line[i].isalnum()):
                        self._tokens.append(Token.END)
                    else:
                       self._tokens.append(Token.INVALID)
                       break

               else:
                  self._tokens.append(Token.INVALID)
                  break
               

           # if no matching tokens found, then currChar represents an invalid token
            else: 
               self._tokens.append(Token.INVALID)
               break


    # Moves cursor to next token in tokens array, unless the current token being pointed at
    # by cursor is 33 (EOF) or 34 (illegal token), in which the cursor is not moved. 
    # If advancing the cursor forward puts it past the last index of the tokens array, the next line from the file is 
    # tokenized into tokens array with tokenizeLine(). 
    def skipToken(self):
       if self.getToken() < 33:
        self._cursor=self._cursor+1
        if self._cursor == len(self._tokens):
         self._tokenizeLine()

    # Returns the token number that is being pointed to in tokens array by cursor.
    def getToken(self):
       return self._tokens[self._cursor].value
    
    # Returns the value of the integer token being pointed to by cursor.
    # If the current token is not an integer, program will exit.
    def intVal(self):
       if self.getToken() == 31:
          # get token from actual_values and check if it has leading zeros, truncating them as necessary
          intToken = self.actual_values[self._cursor]
          while (intToken[0]=='0'):
             intToken = intToken[1:] 
          return int(intToken)
       else:
          print("ERROR: current token is not an integer. Terminating program...")
          sys.exit(1)

    # Returns the value of the identifier token being pointed to by cursor.
    # If the current token is not an identifier, program will exit.
    def idName(self):
       if self.getToken() == 32:
          return self.actual_values[self._cursor]
       else:
          print("ERROR: current token is not an identifier. Terminating program...")
          sys.exit(1)