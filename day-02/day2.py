##Exercise 1 — if, elif, else
age = 25
if age < 13:
    print("Child")
elif 13 <= age <=17:
    print("Teenager")
else:
    print("Adult")


## Exercise 2 — Even or Odd  
#Determine whether the number is even or odd.
number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


##Exercise 3 — Loop through a list
names = ["Yasmine", "Ali", "Esa", "Sara"]

for name in names:
    #print(name, end=", ")
    print(f"Hello {name}!")



##Exercise 4 — Numbers with a loop
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num**2)


##Exercise 5 — range()
for num in range(2,12,2):
    print(num)

##Exercise 6 — Strings
message = "python is fun"
print(message.upper())
print(message.lower())
print(message.capitalize())
print(len(message))


name="Yasmine"
print(name[0])   ##Y
print(name[-1])   ##e


##Exercise 7 — Build a total
## Instead of using sum(), calculate the total yourself using a loop.
numbers = [5, 10, 15, 20]
totel = 0
for num in numbers:
    totel += num

print(totel)


##⭐ Day 2 Challenge

## Create a new list containing only the even numbers.
numbers = [3, 8, 12, 5, 7, 10]  ##even = [8, 12, 10]
even_list=[]
for num in numbers:
    if num % 2 == 0:
        even_list.append(num)

print(even_list)


##⭐ Day 2 Mini LeetCode Challenge
##Find the largest number without using max().
numbers = [4, 2, 9, 7, 5, 1]
largest = numbers[0]
for num in numbers:
    if num >= largest:
        largest = num

print(largest)

