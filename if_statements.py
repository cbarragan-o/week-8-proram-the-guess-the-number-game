def if_statements():
  pass
  ##################### if statements ############################################

  # Decision Making Practice #1
  # Using the variables num1 and num2, which are fed with user input (just like in the provided code), create a flow control structure that compares the values of the variables, and returns a result according to the case:

  # "num1 is greater than num2"

  # "num2 is greater than num1"

  # "num1 and num2 are equal"

  # You must display the value of the user input instead of num1 and num2.
  num1 = int(input("enter a number: "))
  num2 = int(input("enter another number: "))
  if num1 > num2:
    print(num1, "is greater than", num2)
  elif num2 > num1:
    print(num2, "is greater than", num1)
  elif num1 == num2:
    print(num1, "and", num2, "are equal")
  else:
    print("error")
  # Decision Making Practice #2
  # The laws of a certain country establish that an adult can drive if they are of legal age (18 years or older), and have a driver's license.
age = int(input("Enter your age: "))
if age < 18:
  print("You are not eligible to drive ")
elif age >= 18:
  print("You are eligible to drive")
  
  # Create a conditional structure to check if a 16-year-old without a license can drive, and display the corresponding result on the screen:
age = int(input("Enter your age: "))
if age < 18:
  print("you cant drive yet.You must be 18 years old and have a license")
elif age >= 18:
  print("you can drive only if you have your license")
  # "You can drive"

  # "You can't drive yet. You must be 18 years old and have a license"

  # "You can't drive. You need to have a license"

  # Use the code base already provided to set up the appropriate flow control structure and check those conditions.

  # Decision Making Practice #3
  # To access a certain job, the candidate must be able to program in Python and speak French.

  # Create a conditional structure to evaluate a candidate given these conditions, and display the corresponding message on the screen:


  # "You meet the requirements to apply"

  # "To apply, you need to know how to program in Python and speak French"

  # "To apply, you need to speak French"

  # "To apply, you need to know how to program in Python"

  # Use the code already provided to set up the appropriate flow control structure and check those conditions. Evaluate a candidate who knows French, but does not know how to program in Python.


python = input("Do you know how to program in Python? ").lower()
french = input("Do you know how to speak French? ").lower()
if python and french == "yes":
  print("You meet the requirements to apply.")
else:
  print("You do not meet the requirements to apply.")

  ####################end if statements###########################################
