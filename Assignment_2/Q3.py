#Assignment 2 - Q3

import random 
random.seed(1024160050)

#i. 
numbers = [random.randint(100,900) for _ in range(100)]
print(numbers)

#ii. 
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)
print("Count of odd numbers: ", len(odd_numbers))

#iii.
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
print("Count of even numbers: ", len(even_numbers))

#iv. 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
prime_numbers = [num for num in numbers if is_prime(num)]
print(prime_numbers)
print("Count of prime numbers: ", len(prime_numbers))

#v. 
frequency = {} 
for num in numbers: 
    frequency[num] = frequency.get(num, 0) + 1

most_frequent = max(frequency, key=frequency.get)
most_frequent_count = frequency[most_frequent]
print("Most frequent number: ", most_frequent, "Count: ", most_frequent_count)