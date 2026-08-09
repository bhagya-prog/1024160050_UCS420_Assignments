#Assignment 2- Q2
#Using list from Q1.py --> the final changed list
L = [60, 50, 40, 20, 10, 10, 0, 0, 0, 0]

scores = tuple(L[:8])   #(60, 50, 40, 20, 10, 10, 0, 0)
print(scores)

#i. 
highest = max(scores)        #60
highest_index = scores.index(highest)       #at index 0 

lowest = min(scores)       # 0 
lowest_index = scores.count(lowest)     #2

print("Highest Score: ", highest, "Index: ", highest_index)
print("Lowest Score: ", lowest, "Count: ", lowest_index)

#ii. 
reversed_scores = list(reversed(scores))
print(reversed_scores)     #[0,0,10,10,20,40,50,60]

#iii.
user_score = int(input("Enter your score: "))
if user_score in scores: 
    print("First occurence: ", scores.index(user_score))
else : 
    print("Score not found in the tuple")

#iv. 
#scores[0] = 100

#we got a TypeError :  'tuple' object does not support item assignment 
#As tuple is immutable and list are mutable, so we can't change the value of an element after tuple creation. 

#v. 
first_score, second_score, *remaining_scores = scores
print("First Score: ", first_score)       #60
print("Second Score: ", second_score)      #50 
print("Remaining Scores: ", remaining_scores)       #[40, 20, 10, 10, 0, 0]