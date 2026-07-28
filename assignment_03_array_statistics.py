# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def compute_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def compute_average(numbers):
    if not numbers:
        return 0
    total = compute_sum(numbers)
    # Count items using a loop
    count = 0
    for _ in numbers:
        count += 1
    return total / count

def compute_max(numbers):
    if not numbers:
        return None
    highest = numbers[0]
    for num in numbers:
        if num > highest:
            highest = num
    return highest

def compute_min(numbers):
    if not numbers:
        return None
    lowest = numbers[0]
    for num in numbers:
        if num < lowest:
            lowest = num
    return lowest

def main():
    # Get and validate the count
    try:
        n = int(input("How many numbers? "))
    except ValueError:
        print("Error: Input must be an integer.")
        return

    if n <= 0:
        print("Error: Number must be a positive integer.")
        return

    # Collect numbers from the user
    numbers = []
    for i in range(1, n + 1):
        while True:
            try:
                num = float(input(f"Enter number {i}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Calculate statistics
    total_sum = compute_sum(numbers)
    avg = compute_average(numbers)
    maximum = compute_max(numbers)
    minimum = compute_min(numbers)

    # Print results matching the expected format
    print("\nResults:")
    # Format to strip trailing decimal zeros if they are whole numbers
    print(f"Sum:      {int(total_sum) if total_sum.is_integer() else total_sum}")
    print(f"Average:  {int(avg) if avg.is_integer() else avg}")
    print(f"Maximum:  {int(maximum) if maximum.is_integer() else maximum}")
    print(f"Minimum:  {int(minimum) if minimum.is_integer() else minimum}")

if __name__ == "__main__":
    main()

