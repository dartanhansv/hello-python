"""
PEP 498: Literal String Interpolation
    Commonly called f-strings

    "Embed expressions inside literal strings, using a minimal syntax"
"""

print(f"One plus one is {1 + 1}")

x = int(input("Type a number you would like to multiple by itself: "))
result = x * x
print(f"{x} times {x} is equal to: {result} \n")

import datetime
print(f"The current time is {datetime.datetime.now()}")