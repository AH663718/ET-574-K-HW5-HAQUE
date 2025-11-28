def abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError(f"abs() expected int or float, got {type(x).__name__}")
    return x if x >= 0 else -x

def cylinder_volume(radius, height):
    pi = 3.141592653589793
    return pi * radius * radius * height

def cube_volume(x):
    return x * x * x

def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Absolute Value")
        print("2. Volume of a Cube")
        print("3. Volume of a Cylinder")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            try:
                val = float(input("Enter a number for abs(): "))
                print("Absolute value:", abs(val))
            except Exception as e:
                print("Error:", e)

        elif choice == "2":
            try:
                side = float(input("Enter side length of cube: "))
                print("Cube Volume:", cube_volume(side))
            except Exception as e:
                print("Error:", e)

        elif choice == "3":
            try:
                radius = float(input("Enter radius: "))
                height = float(input("Enter height: "))
                print("Cylinder Volume:", cylinder_volume(radius, height))
            except Exception as e:
                print("Error:", e)

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


# Only run the menu if this file is executed directly
if __name__ == "__main__":
    menu()
