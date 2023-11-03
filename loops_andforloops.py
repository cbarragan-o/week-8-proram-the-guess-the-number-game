def loops_andforloops():
  #Christopher Barragan, Santiago Rodriguez, Ignacio Estrada
  ##################loops and for loops###################################
  # For Loops Practice #1
  # Using For loops, greet all members of a class, printing "Hello" + their name.

  # For example: "Hello Norville"

  students = ["Norville", "Fred", "Velma", "Daphne"]
  for student in students:
    print("Hello " + student)


# For Loops Practice #2
# Given the following list of numbers, calculate the sum of all the numbers using For loops and store the result of the sum in a variable called sum_numbers:

list_numbers = [
    1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4
]
my_value = 0
for num in list_numbers:
  sum_numbers = my_value + num
  print(sum_numbers)
# For Loops Practice #3
# Given the following list of numbers, perform the sum of all even and odd* numbers separately in the variables sum_even and sum_odd respectively:

list_numbers1 = [
    1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4
]

sum_even = 0
sum_odd = 0

for num in list_numbers1:
  if num % 2 == 0:
    sum_even += num
  else:
    sum_odd += num

print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)

# *Recall from previous days: the modulus (or remainder) of a number divided by 2 is zero when said value is even, and 1 when it is odd

# num % 2 == 0 (even values)

# num % 2 == 1 (odd values)

################## end loops and for loops###################################
