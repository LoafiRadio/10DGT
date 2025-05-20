def calculator():
    while True:
        try:
            Width = float(input("Enter width: "))
            if Width <= 0:
                print("Width must be bigger than zero.")
                continue
            Height = float(input("Enter height: "))
            if Height <= 0:
                print("Height must be bigger than zero.")
                continue

            Area = Width*Height
            Perimeter = 2*(Width+Height)
            print(f"Area is {Area} squared units")
            print(f"Perimeter is {Perimeter} units")

            another = input("Do you want to perform another calculation? (Yes/No): ").lower()
            if another != 'yes':
                break
        except ValueError:
            print("Invalid input. Please enter numbers only.")

calculator()