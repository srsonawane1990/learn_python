# Pass the arguments to python file
import sys
print("Let's read the arguments from command line")
print(sys.argv)
print(' '.join(sys.argv[1:]).upper())
