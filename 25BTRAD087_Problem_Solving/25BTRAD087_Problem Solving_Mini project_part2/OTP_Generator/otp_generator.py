import secrets
import string

print("========== OTP GENERATOR ==========")
print("1. Numeric OTP (4 digits)")
print("2. Numeric OTP (6 digits)")
print("3. Alphanumeric OTP")

choice = input("Enter your choice (1-3): ").strip()

if choice == "1":
    otp = "".join(secrets.choice(string.digits) for _ in range(4))
    print(f"\nYour 4-digit OTP: {otp}")
elif choice == "2":
    otp = "".join(secrets.choice(string.digits) for _ in range(6))
    print(f"\nYour 6-digit OTP: {otp}")
elif choice == "3":
    while True:
        try:
            length = int(input("Enter OTP length (4-32): "))
            if 4 <= length <= 32:
                break
            print("OTP length must be between 4 and 32.")
        except ValueError:
            print("Invalid input! Enter a whole number.")
    alphabet = string.ascii_uppercase + string.digits
    otp = "".join(secrets.choice(alphabet) for _ in range(length))
    print(f"\nYour OTP: {otp}")
else:
    print("Invalid choice!")
