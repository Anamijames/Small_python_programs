# Simple Calculator program

def add(a, b) :
  sum = a + b
  return sum

def subtract(a, b) :
  diff = a - b
  return diff

def multiply(a, b) :
  mul = a * b
  return mul

def divide(a, b) :
  div = a / b
  return div

def exp(a, b) :
  ex = a ** b
  return ex

print("The sum of numbers 4 and 5 is", add(4, 5))

print("The differences between 49 and 12 is",subtract(49, 12))

print("The product of 12 and 45 is",multiply(12, 45))

print("The numbers 5 and 8 when divided gives",divide(5, 8))

print("3 to the power 6 is",exp(3, 6))