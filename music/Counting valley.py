path = ("DDUUUUDD")
steps = len(path)

print(steps)
valley_count = 0


D_counter = 0
for i in path:
    if i is "D":
        D_counter += 1
    if i is not "D":
        D_counter -= 1
    if i is not "D" or D_counter <= 0:
        continue
    valley_count += 1

print(valley_count)