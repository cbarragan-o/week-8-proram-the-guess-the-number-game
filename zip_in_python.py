def zip_in_python():
  ##########################zip in python#####################################
  names = ['Alice', 'Bob', 'Charlie']
  ages= [23, 34, 45]
  countries = ['USA', 'Canada', 'Mexico']
  
  for name, age, country in zip(names, ages, countries):
    print(f"{name}, aged {age}, from {country}")

  pairs = [("Alice", 23), ("Bob" , 34), ("Charlie", 45)]
  names, ages = zip(*pairs)
  # Zip Practice #1
  # Print to the screen phrases like the following example:

  # "The capital of Germany is Berlin"

  # Use the zip function, loops, and the following lists of countries and capitals to solve it quickly and efficiently.

  capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
  countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]

  for capital, country in zip(capitals, countries):
    print(f"The capital of {country} is {capital}")


  # Zip Practice #2
  # Create a zip object made up of lists, of a set of brands and products that you prefer, inside the my_zip variable.
  product = ["phone", "computer", "monitor", "headphones"]
  brand = ["Apple", "Dell", "Asus", "Sony"]

  for p,b in zip(product, brand):
    print(f"For {p}s, I prefer {b}.")
  # Zip Practice #3
  # Create a zip object with the translations of the numbers from 1 to 5 in Spanish, Portuguese and English (in that same order), and then convert the generated object into a list called numbers:
  
  spanish = ["uno", "dos", "tres", "cuatro", "cinco"]
  portuguese = ["um", "dois", "tres", "quatro", "cinco"]
  english = ["one", "two", "three", "four", "five"]
  numbers = list(zip(spanish, portuguese, english))
  print(numbers)
  


  # uno / um / one

  # dos / dois / two

  # tres / três / three

  # cuatro / quatro / four

  # cinco / cinco / five

  # The result should follow the structure:

  # [('one', 'um', 'one'), ('two', 'dois', 'two'), ...
  #########################zip in python############################################
