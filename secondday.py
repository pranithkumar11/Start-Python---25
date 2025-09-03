def add_with_lines(a, b):
    # Show numbers as sticks
    print(f"{a} → {'|'*a}")
    print(f"{b} → {'|'*b}")
    print('-'*20)
    # Show only the sum as a number
    total = a + b
    print(total)

add_with_lines(5, 9)
