from collections import Counter
ip = [1,2,3,4,45,6,7,8,8,9,9,1,1,1,1,2,2,3,4,45,5,6]
k = 2

c = Counter(ip)
c1 = sorted(c, key=c.get)[:2]
print(c1)
print(c)