# operators are basically the function which can be used to perform an operations
# in python there are 7 operators: airthmetic, comparison

print("<<<<<<<<<Airthmetic Operators>>>>>>>>>")


a = 20
b = 6

print("Addition (+):", a + b)          # 26
print("Subtraction (-):", a - b)       # 14
print("Multiplication (*):", a * b)    # 120
print("Division (/):", a / b)          # 3.3333...
print("Floor Division (//):", a // b)  # 3
print("Modulus (%):", a % b)           # 2
print("Exponent (**):", a ** b)        # 64000000



print("<<<<<<<<<<Assignment Operation>>>>>>>>>>>>")

x = 50
print("Initial value:", x)

x += 15      # x = x + 15
print("Addition Assignment (+=):", x)      # 65

x -= 20      # x = x - 20
print("Subtraction Assignment (-=):", x)   # 45

x *= 4       # x = x * 4
print("Multiplication Assignment (*=):", x) # 180

x /= 5       # x = x / 5
print("Division Assignment (/=):", x)      # 36.0

x //= 7      # x = x // 7
print("Floor Division Assignment (//=):", x) # 5.0

x %= 3       # x = x % 3
print("Modulus Assignment (%=):", x)       # 2.0

x **= 4      # x = x ** 4
print("Exponent Assignment (**=):", x)     # 16.0

x = 12
x &= 10      # Bitwise AND Assignment
print("Bitwise AND Assignment (&=):", x)   # 8

x = 12
x |= 10      # Bitwise OR Assignment
print("Bitwise OR Assignment (|=):", x)    # 14

x = 12
x ^= 10      # Bitwise XOR Assignment
print("Bitwise XOR Assignment (^=):", x)   # 6

x = 12
x <<= 2      # Left Shift Assignment
print("Left Shift Assignment (<<=):", x)   # 48

x = 12
x >>= 2      # Right Shift Assignment
print("Right Shift Assignment (>>=):", x)  # 3

