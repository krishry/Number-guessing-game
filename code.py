import random

n = int(input("Enter the final range for computer to generate a random number (e.g., 10, 100, 1000): "))
x = random.randint(0, n)

def guess_number(start, end):
    if start > end:
        print("Something went wrong with the range.")
        return

    gn = int(input(f"Enter a number between {start} and {end}: "))

    if gn < start or gn > end:
        print("Entered number is out of bounds.")
        guess_number(start, end)
        return

    if gn == x:
        print("Number guessed correctly!")
        return

    mid = (start + end) // 2

    if gn > mid and x < mid:
        print(f"Computer generated number is less than {mid}")
        guess_number(start, mid - 1)
    elif gn < mid and x > mid:
        print(f"Computer generated number is more than {mid}")
        guess_number(mid + 1, end)
    elif gn < mid and x < mid:
        if gn < x:
            print(f"Computer generated number is less than {mid} but still bigger than {gn}")
            guess_number(gn + 1, mid - 1)
        else:
            print(f"Computer generated number is less than {mid} but smaller than {gn}")
            guess_number(start, gn - 1)
    elif gn > mid and x > mid:
        if gn > x:
            print(f"Computer generated number is more than {mid} but smaller than {gn}")
            guess_number(mid + 1, gn - 1)
        else:
            print(f"Computer generated number is more than {mid} but bigger than {gn}")
            guess_number(gn + 1, end)
    else:
        print("Error. Try again.")
        guess_number(start, end)

guess_number(0, n)