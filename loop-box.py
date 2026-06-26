print("Welcome to Logic Box")

while True:
    print("Please choose an option:")
    print("1. Right Angle Triangle")
    print("2. Pyramid")
    print("3. Left Angle Triangle")
    print("4. Analyze Numbers")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        rows = int(input("Enter number of rows: "))
        if rows <= 0:
            print("Invalid rows")
            break
        print("Right Angle Triangle")
        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end=" ")
            print()

    elif choice == 2:
        rows = int(input("Enter number of rows: "))
        print("Pyramid Pattern")
        for i in range(rows):
            for space in range(rows - i - 1):
                print(" ", end="")
            for j in range(2 * i + 1):
                print("*", end="")
            print()

    elif choice == 3:
        rows = int(input("Enter number of rows: "))
        print("Left Angle Triangle")
        for i in range(1, rows + 1):
            for j in range(rows - i):
                print(" ", end=" ")
            for k in range(i):
                print("*", end=" ")
            print()

    elif choice == 4:
        start = int(input("Enter start number: "))
        end = int(input("Enter end number: "))
        if end < start:
            print("End must be greater than start")
            continue

        total = 0
        for i in range(start, end + 1):
            if i == 0:
                pass
            if i % 2 == 0:
                print(i, "is Even")
            else:
                print(i, "is Odd")
            total += i
        print("Sum =", total)

    elif choice == 5:
        print("Thank you")
        break
    else:
        print("Invalid choice")