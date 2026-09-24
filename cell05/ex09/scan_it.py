import sys

num_para = len(sys.argv) - 1

if num_para == 2:
    print(sys.argv[2].count(sys.argv[1]))
else :
    print("none")