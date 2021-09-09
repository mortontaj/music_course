a = [4, 6, 5, 3, 3, 1]

countt = 1
for _ in set(a):
    if (_ + 1 and _ - 1) not in set(a):
        del _

for i in set(a):
    if a.count(i) + a.count(i + 1) > countt:
         countt = a.count(i) + a.count(i + 1)

print(countt)