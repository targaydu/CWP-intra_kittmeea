import sys

num_para = len(sys.argv) - 1

if num_para == 1:
    print(sys.argv[1].lower())
else :
    print("none")