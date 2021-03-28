
from art import logo

def add(n1, n2):
  return n1 + n2

def minus(n1, n2):
  return n1 - n2

def divide(n1, n2):
  return n1/n2

def multiply(n1, n2):
  return n1*n2

#key operations
keys = {
  "+": add,
  "-": minus, 
  "/": divide, 
  "*": multiply
  }

def calculator():
  print(logo)
  num1 = float(input("enter your number?\n"))
  should_continue = True
  while should_continue:
    for i in keys:
      print(i)
    operations = input("please pick an operation?")
    num2 = float(input("enter your second number? \n"))
    total = keys[operations]
    total = total(n1 = num1, n2= num2)
    print(f"{num1} {operations} {num2} = {total}")
    if input("do you want to continue?\n press 'y' for yes or 'n' for no\n") == "y":
      num2 = total
    else:
      should_continue == False
      calculator()

calculator()






