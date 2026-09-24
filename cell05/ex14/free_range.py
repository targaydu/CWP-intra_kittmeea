import sys

num_para = len(sys.argv) - 1
mylst = list()

if num_para == 2:
    if int(sys.argv[1]) <= int(sys.argv[2]):
        for i in range(int(sys.argv[1]), int(sys.argv[2])+1, 1):
            mylst.append(i)
    else:
        for i in range(int(sys.argv[1]), int(sys.argv[2])-1, -1):
            mylst.append(i)
    print(mylst)
else :
    print("none")