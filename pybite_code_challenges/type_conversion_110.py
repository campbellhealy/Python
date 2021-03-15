# type_conversion_110.py

from decimal import Decimal

def divide_numbers(numerator, denominator):
   try:
      result = round(int(numerator))/ round(int(denominator))
      result = Decimal(result)
      
   except ValueError:
      print(f'There was a ValueError with {numerator}/{denominator}')
      result = 'No Result'
      
   except ZeroDivisionError:
      print(f'There was a ZeroDivisionError with {numerator}/{denominator}')
      result = 0
   
   return result






# divide_numbers()
print(divide_numbers(1, 2))  # int -> float 0.5
print(divide_numbers(8, 2)) # int -> int 4
print(divide_numbers('3', '2')) # str -> int -> float 1.5
print(divide_numbers(8.2, 2)) # float, int -> int 4
print(divide_numbers(1, 2.9)) # int, float -> float 0.5
print(divide_numbers(2, 0))
print(divide_numbers('s', 2)) 
print(divide_numbers('v', 'w')) 

