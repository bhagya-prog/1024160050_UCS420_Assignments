#Assignment 2 - Q5
my_dict = {
    "name": "Bhagya Vardhan",
    "roll_no": "1024160050",
    "branch" : "Computer Science and Engineering",
    "age": 20,
    "city": "Jalandhar"
}
print("Original dictionary")
print(my_dict)

# i.
my_dict["location"] = my_dict.pop("city")
print(my_dict)

#ii.
my_dict["cgpa"] = 9.19
print(my_dict)

#iii.
my_dict["age"] += 1
print(my_dict)

#iv.
#Pop returns the value of that key deleted and then deletes it
dict_pop = my_dict.copy()
removed_branch = dict_pop.pop("branch")
print(dict_pop)
print(removed_branch)

#Delete just removes the key-value pair
dict_del = my_dict.copy()
del dict_del["branch"]
print(dict_del)

#v.
for key, value in my_dict.items():
  print(f"{key}--> {value}")

#vi.
if("email" in my_dict) :
  print("Email : " , my_dict["email"])
else :
  print("Email doesn't exist in dictionary")

#vii.
friend_dict = {
    "name": "Dhiren Kumar",
    "roll_no": "1024160042",
    "branch": "Computer Science and Engineering",
    "age": 20 ,
    "city": "Sangroor"
}
print(friend_dict)
#When values are common the values from friend_dict win over the ones in my_dict
#As friend_dict is written later in merged_dict
merged_dict = {**my_dict, **friend_dict}
print("Merged dictionary is: ", merged_dict)

#viii.
#Here isinstance check if v is str or not , and if it is str then only add in string_dict
string_dict = {k : v for k , v in my_dict.items() if isinstance(v, str)}
print(string_dict)