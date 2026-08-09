#ASSIGNMENT 2 - Q1
roll_no = "1024160050"

# i.
L = [int(digit) * 10 for digit in roll_no]
print(L)

#ii.
#Original List ---> [10, 0, 20, 40, 10, 60, 0, 0, 50, 0]
L.append(66)
print(L)
#Changed List ---> [10, 0, 20, 40, 10, 60, 0, 0, 50, 0, 66]
#Using append we can add something to end of List, hence 66 is added to the end

L.insert(1, 44)
print(L)
#Changed List ---> [10, 44, 0, 20, 40, 10, 60, 0, 0, 50, 0, 66]
#Insert adds something at a specific index in the list, like 44 is added at index 1

#iii.
L.remove(44)
print(L)
#Changed List ---> [10, 0, 20, 40, 10, 60, 0, 0, 50, 0, 66]

L.pop()
print(L)
#Changed List ---> [10, 0, 20, 40, 10, 60, 0, 0, 50, 0]

#iv.
L.sort()
print(L)
#Changed List ---> [0, 0, 0, 0, 10, 10, 20, 40, 50, 60]
L.sort(reverse = True)
print(L)
#Changed List ---> [60, 50, 40, 20, 10, 10, 0, 0, 0, 0]

#v.
#Here using the sorted list only in reverse manner
print("First three elements")
print(L[0:3])      #[60,50,40]
print("Last three elements")
print(L[-3:])   #   #[0,0,0]

#vi.
average = sum(L)/ len(L)
new_list = []
print(average)     #19.0
for s in L:
  if (s > average):
    new_list.append(s)

print(new_list)    #[60, 50, 40, 20]
