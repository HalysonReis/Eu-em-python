num = [1,2,3,4,5.0,7.0,9.0,6.0]

num.pop()
num.pop()
print(num)

num.insert(7, 66)
print(num)

print(num[-3])
num.remove(5.0)
print(len(num))
print(sum(num))
print(sum(num) / len(num))
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(max(num))
print(min(num))