f = list(open("input.txt").read().strip())
print(next(i for i in range(4,len(f)) if len(set(f[i-4:i])) == 4))
print(next(i for i in range(14,len(f)) if len(set(f[i-14:i])) == 14))