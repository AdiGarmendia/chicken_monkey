# Write a program that prints the numbers from 1 to 100. You can use Python's range() 
# to quickly make a list of numbers.
numbers = list(range(1, 101))
print(numbers)
# For multiples of five (5, 10, 15, etc.) print "Chicken" instead of the number.
for num in numbers:
  if num % 5 == 0 and num % 7 == 0:
    print("ChickenMonkey")
# For the multiples of seven (7, 14, 21, etc.) print "Monkey".
  elif num % 7 == 0:
    print("Monkey")
# For numbers which are multiples of both five and seven print "ChickenMonkey".
  elif num % 5 == 0:
    print("Chicken")
  else:
    print(num)
#not sure why but I had to move the 5 and 7 to the if and move the single 5 to a elif
# To determine if a number can be evenly divided by 5 or 7, use the Python modulo operator.