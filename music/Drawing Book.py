nn = 20
pp = 15

if pp % 2 == 1:
    pp -= 1
if nn // 2 > pp:
    print(pp // 2)
else:
    print((nn // 2) - (pp // 2))
