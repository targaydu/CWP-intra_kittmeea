import sys

num_para = len(sys.argv) - 1

if num_para == 1:
    txt = input("What was the parameter? ")
    if txt == sys.argv[1]:
        print("Good Job!")
    else :
        print("Nope, sorry...")
else :
    print("none")