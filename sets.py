# Sets is a collection of non repetiative data points or it contains unique values
# properties of sets are they aur mutable, and heterogeneous, and store unique values, unordered, did not allow duplicate values

# set_0 = {2,45,6,1,16,1,32,32}
# set_1 = {45,6,8,2,58,2,5,7,8}
# print("this is my set:", set_0)
# print("type of my set:", type(set_0))
# print("length of my set:", len(set_0))

# set_0.add(65) # add 65 in set
# set_0.discard(32) # remove 32 from set
# set_0.discard(0) # does not show any error although 0 is not in set

# # print(set[0:3])  this will show error because sets are not subscriptable 
# # print(set[0])  this will also s
# print(set_0)

# lst = [1,51,6,6]
# print(set(lst)) # typecasting of list into set


# Sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union (all unique elements)
print("Union:", A.union(B))          # {1, 2, 3, 4, 5, 6}

# Intersection (common elements)
print("Intersection:", A.intersection(B))  # {3, 4}

# Difference (elements in A but not in B)
print("Difference:", A.difference(B))      # {1, 2}

# Subset (is every element of A present in B?)
print("Is {1,2} subset of A?", {1, 2}.issubset(A))  # True

# Superset (does A contain all elements of another set?)
print("Is A superset of {1,2}?", A.issuperset({1, 2}))  # True

# intersection_update (modifies the original set)
C = {1, 2, 3, 4}
C.intersection_update(B)
print("After intersection_update:", C)  # {3, 4}

print(2 in A)



