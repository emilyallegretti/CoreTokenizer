from enum import Enum

# Enum class associating each Core token type with a unique value. These values are used by the Scanner when tokenizing input programs. 
class Token(Enum):
    # SPECIAL CHARACTERS
    PROGRAM = 1
    BEGIN = 2
    END = 3
    INT = 4
    IF = 5
    THEN = 6
    ELSE = 7
    WHILE = 8
    LOOP = 9
    READ = 10
    WRITE = 11

    # SPECIAL SYMBOLS
    SEMICOLON=12
    COMMA=13
    ASSIGN=14
    NOT=15
    OPEN_BRACKET=16
    CLOSE_BRACKET=17
    AND=18
    OR=19
    OPEN_PAREN=20
    CLOSE_PAREN=21
    PLUS=22
    MINUS=23
    ASTERISK=24
    NOT_EQUALS=25
    EQUALS=26
    LESS_THAN=27
    GREATER_THAN=28
    LT_EQUALS=29
    GT_EQUALS=30

    #INTEGERS
    NUMBER=31
    #IDENTIFIER
    ID=32
    #EOF
    EOF=33
    #ILLEGAL TOKEN
    INVALID=34
