import sys
import Scanner

# main driver function for the Core Tokenizer.
# expects 1 command line argument: the name of the input file.
# this function prints out the list of tokens scanned from the input file with Scanner.
def main(args):
    scanner = Scanner(args[1])
    nextToken = scanner.getToken()
    # repeatedly print out token and get next one in scanner,
    # until end-of-file or invalid token is reached
    while (1):
        print(nextToken + "/n")
        if nextToken < 33:
            scanner.skipToken()
            scanner.getToken()
        else:
            break
    

main(sys.argv)