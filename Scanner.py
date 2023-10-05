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
        # keep interal cursor of where we are at in tokens array (so as not to modify the cursor used in skipToken())
        tempCursor=self._cursor
        line = (self.input).readline()
        # analyze each character in the line to determine its token
        i=0
        while i < len(line):
            char = line[i]
        # CASES: 
        
        # WHITESPACE
            #if char == ' ':


        # INTEGERS
            if char.isdigit():
               # begin building string of digits now that we've come across one decimal digit--digitString will hold this string
               digitString=char
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
               self.actual_values[tempCursor] = int(digitString)
               tempCursor=tempCursor+1          

        # IDENTIFIERS
            elif char.isupper():
               # begin building identifier string now that we've come across an identifier character--idString will hold this string
               idString=char
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
               self.actual_values[tempCursor] = idString
               tempCursor = tempCursor+1

        # SPECIAL CHARACTERS
            elif char==";":
               self._tokens.append(Token.SEMICOLON)
               tempCursor=tempCursor+1

            elif char==",":
               self._tokens.append(Token.COMMA)
               tempCursor=tempCursor+1

            elif char == "[":
               self._tokens.append(Token.OPEN_BRACKET)
               tempCursor = tempCursor+1

            elif char=="]":
               self._tokens.append(Token.CLOSE_BRACKET)
               tempCursor=tempCursor+1

            elif char=="(":
               self._tokens.append(Token.OPEN_PAREN)
               tempCursor=tempCursor+1 

            elif char==")":
               self._tokens.append(Token.CLOSE_PAREN)
               tempCursor=tempCursor+1

            elif char == "+":
               self._tokens.append(Token.PLUS)
               tempCursor = tempCursor+1

            elif char == "-":
               self._tokens.append(Token.MINUS)
               tempCursor = tempCursor+1

            elif char == "*":
               self._tokens.append(Token.ASTERISK)
               tempCursor = tempCursor+1

            elif char=="&":
               # check to see if next character is also an ampersand; if not, this token is illegal
               i=i+1
               if (i<len(line) & line[i] == "&"):
                  self._tokens.append(Token.AND)
                  tempCursor=tempCursor+1
               else:
                  self._tokens.append(Token.INVALID)
                  print(self.error_message)
                  break
               
            elif char == "|":
               # check to see if next character is also a vertical bar; if not, this token is illegal
               i = i+1
               if (i < len(line) & line[i] == "|"):
                  self._tokens.append(Token.OR)
                  tempCursor = tempCursor+1
               else:
                  self._tokens.append(Token.INVALID)
                  print(self.error_message)
                  break
               
            elif char == "!":
               # check to see if next character is an equals sign for 'greedy tokenizing'
               i = i+1
               if (i < len(line) & line[i] == "="):
                  self._tokens.append(Token.NOT_EQUALS)
               else: # otherwise just add not symbol
                  self._tokens.append(Token.NOT)
               tempCursor=tempCursor+1

            elif char == ">":
               # check to see if next character is an equals sign for 'greedy tokenizing'
               i = i+1
               if (i < len(line) & line[i] == "="):
                  self._tokens.append(Token.GT_EQUALS)
               else: #otherwise just add GT symbol
                  self._tokens.append(Token.GREATER_THAN)
               tempCursor = tempCursor+1
                  
            elif char == "<":
               # check to see if next character is an equals sign for 'greedy tokenizing'
               i = i+1
               if (i < len(line) & line[i] == "="):
                  self._tokens.append(Token.LT_EQUALS)
               else: #otherwise just add LT symbol
                  self._tokens.append(Token.LESS_THAN)
               tempCursor = tempCursor+1

            elif char == "=":
               # check to see if next character is an equals sign for 'greedy tokenizing'
               i = i+1
               if (i < len(line) & line[i] == "="):
                  self._tokens.append(Token.EQUALS)
               else: #otherwise just add single equals symbol
                  self._tokens.append(Token.ASSIGN)
               tempCursor=tempCursor+1

        # RESERVED WORDS
        



    # Moves cursor to next token in tokens array, unless the current token being pointed at
    # by cursor is 33 (EOF) or 34 (illegal token), in which the cursor is not moved. 
    # If advancing the cursor forward puts it past the last index of the tokens array, the next line from the file is 
    # tokenized into tokens array with tokenizeLine(). 
    def _skipToken(self):
       if self.getToken() < 33:
        self._cursor=self.cursor+1
        if self._cursor == len(self._tokens):
         self._tokenizeLine(self)

    def intVal(self):
       return
    def idName(self):
       return