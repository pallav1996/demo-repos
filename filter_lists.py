print("Filtering odd numbers in a list")

l = [1,2,3,4,5]
print(l)

d = list(filter(lambda x: x%2 == 0, l))
print(d)