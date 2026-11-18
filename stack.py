# Stack Operations

stack = []

while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Reverse String")
    print("5. Reverse Stack using Another Stack")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = input("Enter element: ")
        stack.append(value)
        print("Element pushed successfully")

    elif choice == 2:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Popped element:", stack.pop())

    elif choice == 3:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Stack:", stack[::-1])

    elif choice == 4:
        string = input("Enter a string: ")
        temp = []

        for ch in string:
            temp.append(ch)

        reverse = ""

        while len(temp) > 0:
            reverse = reverse + temp.pop()

        print("Reversed string:", reverse)

    elif choice == 5:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            temp = []

            while len(stack) > 0:
                temp.append(stack.pop())

            stack = temp

            print("Reversed stack:", stack[::-1])

    elif choice == 6:
        print("Program ended")
        break

    else:
        print("Invalid choice")
