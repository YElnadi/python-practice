#Variables and basic data types
name="Yasmine"
age = 35
height='5.10'
is_learning_python="learning Python is fun"

print("my name is",name)
print("my name is",age)
print("my height is",height)
print(is_learning_python)


##Simple calculations
#write python code to solve: Add 15 + 27, sub 18 from 100 multiply 12 x 8
#divide 100 by 7
#find the remainder when 17 is divided by 5

Add = 15 + 27
sub = 100 - 18
multiply = 12 * 8
divide = 100/7
find_reminder = 17%5

print("Add =",Add)
print("sub=",sub)
print("multiply=",multiply)
print("divide=",divide)
print("remainder=",find_reminder)



###Part 3: If Statements
age = 20
if age >= 18:
    print("Adult")
else:
    print("minor")

#### Part 4: Lists
numbers = [5,10,15,20,25]

# prin the first num
print(numbers[0])
#print last number
print(numbers[-1])
print(numbers[len(numbers)-1])
#add 30 to the list 
numbers.append(30)
print(numbers)
#print how many numbers are in the list 
print(len(numbers))
print(numbers)




##part 5 Loops
numbers = [1,2,3,4,5,6]
## write a loop that prints all numbers
for num in numbers:
    print(num**2)


#### Part 6 Functions
## create a function called greet that takesin name and print hello yasmine!
def greet(name):
    print(f"Hello {name}!")

greet("Yasmine")


## creat a function that return the sum of two numbers
##def sum (a,b):
    ##print(f"the sum of {a} and {b} = {a+b}")

##sum(3,7)

##Day 1 LeetCode-style challenge
##given numbers = [2, 7, 11, 15]  target = 9
##Find two numbers whose sum equals the target

numbers = [2, 7, 11, 15]  
target = 9

new_list = []
for i in range(len(numbers)):
    for j in range (i+1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            new_list.append(numbers[i])
            new_list.append(numbers[j])

print(new_list)


##  Write Python code to find:
## Fastest response
## Slowest response
## Average response time

response_times = [1.2, 0.9, 1.5, 1.1, 1.3]

print(f"Number of experiments = {len(response_times)}")
print(f"The Fastest response ={min(response_times)}")
print(f"The Slowest response ={max(response_times)}")


print(f"The Average = {sum(response_times)/len(response_times)}")






