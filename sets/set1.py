my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(5)
my_set.add("hello")
my_set.add(2)
my_set.add(3)

print(type(my_set))
print(my_set)

my_set.remove("hello")
print(my_set)

my_set.discard(4)

my_set2 = {35, 28, 12, 87, 50}
my_set3 = {108, 63, 28, 41, 3}

print(my_set2 | my_set3) # union
print(my_set2 & my_set3) # intersection
print(my_set2 - my_set3) # difference
print(my_set3 - my_set2)
print(my_set2 ^ my_set3) # symmetric difference