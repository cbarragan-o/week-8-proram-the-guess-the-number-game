def enumerator_in_python():
  # Christopher Barragan, Santiago Rodriguez
  ###################enumerator in python########################################
  seasons = ["Spring", "Summer", "Fall", "Winter"]
  for count, season in enumerate(seasons, start=1):
    print(count, season)
  
  # Enumerator Practice #1
  # Print sentences like the following on the screen:

  # '{name} is found at index {index}'
  
  # Where name must be each of the names in the list below, and the index, must be obtained via enumerate().

  # You can use the given print() line as an example and change its variable names, but the returned phrases must be the same!

  # Tip: use loops!

  list_names1 = ["Steven", "Jackie", "Donna", "Kelso", "Eric", "Fez", "Kitty", "Red"]
  for number, name in enumerate(list_names1, start=1):
    print(number, name)

  
  # Enumerator Practice #2
  # Create a list formed by the tuples (index, element), obtained through enumerating the indices of each character of the "Python" string.
  

  # Call the returned list with the variable name indices_list.



  # Enumerator Practice #3
  # Print to the screen only the indices of those names in the list below, that start with M:

  list_names = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"]
  for count, name in enumerate(list_names, start=1):
    if name[0] == "M":
      print(count, name)

  # You can solve it in different ways, but it will help you keeping mind some (if not all) the following elements:

  # loops

  # if conditionals

  # the enumerate() method

  # string methods and indexing
  ###############################enumerator in python###############################12232131
