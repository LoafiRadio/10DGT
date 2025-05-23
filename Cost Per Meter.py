def calculator():
    while True:
        try:
            Width = float(input("Enter width: "))
            if Width <= 0:
                print("Width must be bigger than zero.")
                continue
            Length = float(input("Enter Length: "))
            if Length <= 0:
                print("Length must be bigger than zero.")
                continue
            CostPerM = float(input("Enter cost per meter: "))
            if CostPerM <= 0:
                print("Cost per meter must be bigger than zero.")
                continue

            Perimeter = 2*(Width+Length)
            Cost = CostPerM*Perimeter
            print(f"The cost to fence your {Perimeter}m perimeter rectangular area is ${Cost}")

            another = input("Do you want to perform another calculation?: ").lower()
            if another != '':
                print("Thank you for using the calulator")
                break
        except ValueError:
            print("Invalid input. Please enter numbers only.")

calculator()