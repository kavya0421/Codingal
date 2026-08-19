
def bits(number):
    return format(number, "04b")


secret_code = int(input("Enter the secret code (0-15): "))
access_key = int(input("Enter the access key (0-15): "))

if not (0 <= secret_code <= 15 and 0 <= access_key <= 15):
    print("Please enter numbers between 0 and 15.")
else:
    print("\nBinary values:")
    print("Secret code:", bits(secret_code))
    print("Access key:", bits(access_key))

    print("\nBitwise operations:")
    print("AND:", bits(secret_code & access_key))
    print("OR:", bits(secret_code | access_key))
    print("NOT:", bits((~secret_code) & 0b1111))
    print("XOR:", bits(secret_code ^ access_key))

    print("\nBit shifts:")
    print("Left shift:", bits(secret_code << 1))
    print("Right shift:", bits(secret_code >> 1))

    print("\nOdd or even using XOR:")
    toggled_value = secret_code ^ 1
    print("After toggling the last bit:", toggled_value)
    print("Binary value:", bits(toggled_value))

    print("\nNumber of 1 bits:", secret_code.bit_count())
