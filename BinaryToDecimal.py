def binary_to_decimal(binary_str):
    return int(binary_str,2)

binary_str = input("Enter a binary number:")

if all(c in '01' for c in binary_str):
    decimal_value = binary_to_decimal(binary_str)
    print(f"The decimal value of binary{binary_str} is {decimal_value}")
else:
    print("Invalid input.Please enter a valid binary number.")