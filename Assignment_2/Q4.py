#Assignment 2 - Q4

L = [1,0,2,4,1,6,0,0,5,0]
A = {digit*7 for digit in L}
B = {digit*9 for digit in L}
print("Set A: ", A)
print("Set B: ", B)

#i. 
union = A.union(B)
print("Union of A and B: ", union)

#ii. 
intersection = A.intersection(B)
print("Intersection of A and B: ", intersection)

#iii.
A_minus_B = A.difference(B)
B_minus_A = B.difference(A)

#symmetric difference () gives all values that are in either set but not in both 
#While differene () gives all values only in one set and not the other

#iv. 
symmetric_diff = A.symmetric_difference(B)
print("Symmetric difference of A and B: ", symmetric_diff)

#v. 
print("Is A a subset of B? ", A.issubset(B))
print("Is B a superset of A", B.issuperset(A))

#vi. 
X = int(input("Enter a number to remove from set A: "))
A.discard(X)  
print("Set A after removing", X, ": ", A)

#discard() is safer because it doesn't raise a KeyError when value is not found in the set 