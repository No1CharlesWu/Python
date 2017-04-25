n = int(input())
s = set(map(int, input().split()))
m = int(input())
for i in range(m):
    tmp = list(input().split())
    if tmp[0] == 'pop':
        s.pop()
    elif tmp[0] == 'discard':
        s.discard(int(tmp[1])
    elif tmp[0] == 'remove':
        s.remove(int(tmp[1]))
print(len(s))