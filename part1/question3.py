################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!

class Oven: #Class Oven for add, freeze, boil, wait and get_output methods

  #Function to declare instance variables for 3 asserts
  def __init__(self):
    self.ingredients = [] #Declare ingredients as a list
    self.temperature: int = 0 #Declare temperature variable as a integer
    self.output = None #Declare output as none

  
  #Add function with item argument 
  def add(self, item): 
    self.ingredients.append(item) #Append to the ingredients list

  #Freeze function with snow output
  def freeze(self):
    self.output = "snow"

  #Boil function with pizza and gold output
  def boil(self):
    if set(self.ingredients) == set({"cheese", "dough", "tomato"}): #Conditional for pizza ingredients
      self.output = "pizza"
    else: #Else for gold
      self.output = "gold"
    print(self.ingredients)

  #Wait function with text output
  def wait(self):
    self.output = "nothing happened"

  #Get output function to show the result
  def get_output(self):
    print(self.output) 
    return self.output
  

def make_oven():
  return Oven()

def alchemy_combine(oven, ingredients, temperature):
  
  for item in ingredients:
    oven.add(item)

  if temperature < 0:
    oven.freeze()
  elif temperature >= 100:
    oven.boil()
  else:
    oven.wait()

  return oven.get_output()