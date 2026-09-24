import sys

num_para = len(sys.argv) - 1

if num_para >= 1:
    for i in range(1, num_para+1, 1):
        if sys.argv[i][-3:] == "ism":
            pass
        else:
            print(f"{sys.argv[i]}ism")
else :
    print("none")