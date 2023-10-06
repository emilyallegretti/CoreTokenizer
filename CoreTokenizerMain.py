import sys
from Scanner import *

# main driver function for the Core Tokenizer.
# expects 1 command line argument: the name of the input file.
# this function prints out the list of tokens scanned from the input file with Scanner.
def main(args):
    print(args[1])
    scanner = Scanner(args[1])
    nextToken = scanner.getToken()
    # repeatedly print out token and get next one in scanner,
    # until end-of-file or invalid token is reached
    while (1):
        print(nextToken)
        if nextToken < 33:
            scanner.skipToken()
            nextToken = scanner.getToken()
        else:
            if nextToken == 33:
                print('End of file reached.')
            else:
                print("ERROR: Invalid Token. Scanner aborted.")
            break
    

main(sys.argv)