Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> temperature =float(input("Enter the temperature value: "))
Enter the temperature value: 25
>>> unit = input("enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ")
enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): C
>>> if unit == "C":
...     fahrenheit = (temperature *9/5) + 32
...     kelvin = temperature + 273.15
...     print("Fahrenheint:", fahrenheint)
...     print ("Kelvin:", kelvin)
... elif unit == "F":
...     celsius = (temperature - 32) * 5/9
...     kelvin = celsius + 273.15
...     print("Celsius:", celsius)
...     print("Fahrenheit:", fahrenheit)
... elif unit == "K":
...     celsius = temperature - 273.15
...     fahrenheit = (celsius * 9/5) + 32
...     print("Celsius:", celsius)
...     print("Fahrenheit:", fahrenheit)
... else:
...     print("Invalid Unit")
