import sys

num_para = len(sys.argv) - 1

if num_para == 1:
    for i in sys.argv[1]:
        if i == "z":
            print("z", end="")
        else:
            pass
    print("")
else :
    print("none")