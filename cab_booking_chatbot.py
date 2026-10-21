import random

while True:
    print("\n1. Book Ride")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("1. Auto - Rs.12/km")
        print("2. Sedan - Rs.18/km")
        print("3. SUV - Rs.25/km")

        cab = input("Choose cab: ")

        if cab == "1":
            name, rate = "Auto", 12
        elif cab == "2":
            name, rate = "Sedan", 18
        elif cab == "3":
            name, rate = "SUV", 25
        else:
            print("Invalid cab!")
            continue

        print("1. Pune Station to Shivajinagar - 5 km")
        print("2. Swargate to Kothrud - 8 km")
        print("3. Hinjawadi to Wakad - 10 km")

        route = input("Choose route: ")

        if route == "1":
            source, dest, km = "Pune Station", "Shivajinagar", 5
        elif route == "2":
            source, dest, km = "Swargate", "Kothrud", 8
        elif route == "3":
            source, dest, km = "Hinjawadi", "Wakad", 10
        else:
            print("Invalid route!")
            continue

        print("Cab:", name)
        print("Route:", source, "to", dest)
        print("Distance:", km, "km")
        print("Total Fare: Rs.", rate * km)

        confirm = input("1. Confirm  2. Cancel: ")

        if confirm == "1":
            print("OTP:", random.randint(1000, 9999))
            print("Booking confirmed. No cancellation after OTP.")
        else:
            print("Ride cancelled. OTP not shared.")

    elif choice == "2":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")