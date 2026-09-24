import sys

num_para = len(sys.argv) - 1

if num_para >= 1:
    print(f"parameters : {num_para}")
    for i in range(1, num_para + 1, 1) :
        print(f"{sys.argv[i]} : {len(sys.argv[i])}")
else :
    print("none")