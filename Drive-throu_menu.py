# Drive_thru menu

def welcome() :
  print("Welcome to FastFood Junction")
  print("****************************")
  print("\tThe Menu")
  print("****************************")
  print("1. 🍔 Cheeseburger")
  print("2. 🍟 Fries")
  print("3. 🥤 Soda")
  print("4. 🍦 Ice Cream")
  print("5. 🍪 Cookie")
  print("")

welcome()


def get_item(x) :
  if x == 1 :
    return '🍔 Cheeseburger'
  elif x == 2 :
    return '🍟 Fries'
  elif x == 3 :
    return '🥤 Soda'
  elif x == 4 :
    return '🍦 Ice Cream'
  elif x == 5 :
    return '🍪 Cookie'

op = int(input("What would you like to order? "))

print("")

print("Your order is", get_item(op))