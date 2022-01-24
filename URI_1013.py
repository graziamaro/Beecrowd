ent = input().split()
a, b, c = int(ent[0]), int(ent[1]), int(ent[2])

maior = (a + b + abs(a-b))/2
result = (maior + c + abs(maior-c))/2

print ("%d eh o maior" %result)
