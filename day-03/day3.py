'''
Exercise 1 — Functions
Create a function that prints a greeting.
'''
def greet(name):
    print(f"Hello {name}!")

greet("Yasmine")
greet("Ali")
greet("Esa")

'''Exercise 2 — return'''
def add(a,b):
    return a + b

result = add(5,7)
print(result)

def multiply(a,b):
    return a * b

result = multiply(5,7)
print(result)

'''Exercise 3 — Function with if'''
def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
    
print(even_or_odd(7))
print(even_or_odd(10))


'''Exercise 4 — User input'''
'''name = input("What is your name?")
print(f"Hello {name}!")

age = int(input("How old are you?"))
if age > 18:
    print("Adult")
else:
    print("Minor")'''

'''Exercise 5 — while loop'''

num = 1
while num <=5:  ##keep doing this while condition is true
    print(num)
    num+=1 


'''Exercise 6 — Find a number in a list'''

numbers = [4, 8, 15, 16, 23, 42]
target = 150

found = False
for num in numbers:
    if num == target:
        found = True
print(found)


'''Exercise 7 — Count even numbers'''
numbers = [3, 8, 12, 5, 7, 10, 14]

count = 0
for num in numbers:
    if num % 2 == 0:
        count +=1

print(count)

'''⭐ Day 3 Challenge'''
'''Find the index of the target.'''
numbers = [5, 10, 15, 20, 25]
target = 20

for i in range (len(numbers)):
    if target == numbers[i]:
        print(f"index={i}")
    

'''⭐ Day 3 Mini LeetCode Challenge'''
'''Create a new list containing the numbers in reverse order, but don't use:'''
numbers = [1, 2, 3, 4, 5]
reverse_list=[]
for i in range(len(numbers)-1, -1, -1):
    reverse_list.append(numbers[i])

print(reverse_list)
