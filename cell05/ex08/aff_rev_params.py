import sys

num_para = len(sys.argv) - 1

if num_para > 1:
    for i in range(num_para, 0, -1):
        print(sys.argv[i])
else :
    print("none")