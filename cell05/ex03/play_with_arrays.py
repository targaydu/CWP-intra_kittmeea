orig = [2, 8, 9, 48, 8, 22, -12, 2]
new = list()
remove_duplicate = set()

for i in orig:
    if i >= 5:
        new.append(i+2)
    else:
        pass

remove_duplicate.update(new)

print("Original array:", orig)
print("New array:", remove_duplicate)