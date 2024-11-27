# This script serves the purpose of testing numeral systems in Python

# Decimal (Base 10) = (int(binary_number))
number = 42
print(number)

# Binary (Base 2)
binary_number = 0b101010 #output is 42
print(f"The binary of '0b101010' shown as a decimal: {binary_number}")

# Conversion to Binary:
decimal = 42
binary = bin(decimal)
print(f"Converting a decimal number into binary: {binary}")

# Octal (Base 8)
octal_number = 0o52
print(f"The octal numeral '0o52' shown as a decimal: {octal_number}")

# Converting to Octal
decimal = 42
octal = oct(decimal)
print(f"Converting a decimal number into octal: {octal}")

# Hexadecimal (Base 16)
hex_number = 0x2A
print(f"The hex numeral '0x2A' shown as a decimal: {hex_number}")

# Converting to Hexadecimal
decimal = 42
hexadecimal = hex(decimal)
print(f"Converting a decimal number into binary: {hexadecimal}")

#Converting any other numeral system into a decimal integer. Note: If the numeral system being converted into Base 10 is a string literal, you must include int(value, base) the string literal's base information as the second argument.
decimal_from_binary = (int(binary_number))
decimal_from_octal = (int(octal_number))
decimal_from_hex = (int(hex_number))
print(f"Converting decimal from binary_number: {decimal_from_binary}, Converting decimal from octal_number: {decimal_from_octal}, Converting decimal from hex_number: {decimal_from_hex}")