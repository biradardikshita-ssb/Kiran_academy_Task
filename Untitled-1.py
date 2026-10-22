print("Welcome to Cab Booking Chatbot!")

name = input("Enter your name: ")
pickup = input("Enter pickup location: ")
drop = input("Enter destination: ")

print("\nChoose your cab:")
print("1. Mini - Rs. 100")
print("2. Sedan - Rs. 200")
print("3. SUV - Rs. 300")

choice = input("Enter your choice (1-3): ")

if choice == "1":
    cab = "Mini"
    fare = 100
elif choice == "2":
    cab = "Sedan"
    fare = 200
elif choice == "3":
    cab = "SUV"
    fare = 300
else:
    cab = None

if cab:
    print("\n--- Booking Confirmed ---")
    print("Name:", name)
    print("Pickup:", pickup)
    print("Destination:", drop)
    print("Cab:", cab)
    print("Fare: Rs.", fare)
    print("Thank you for booking!")
else:
    print("Invalid choice. Please try again.")