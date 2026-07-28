# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def print_fibonacci_sequence():
    """PART A: Asks for N terms and prints the first N Fibonacci numbers."""
    print("--- PART A: Print the First N Terms ---")
    
    # Input validation: Ensure N is a positive integer
    while True:
        try:
            n = int(input("How many terms? "))
            if n > 0:
                break
            else:
                print("Please enter a positive integer greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
    # Generate and print the sequence
    print("Fibonacci sequence: ", end="")
    a, b = 0, 1
    for i in range(n):
        if i == n - 1:
            print(a)  # Prints the last item without a trailing space
        else:
            print(a, end=" ")
        a, b = b, a + b


def check_fibonacci_number():
    """PART B: Asks for a number and checks if it belongs to the sequence."""
    print("\n--- PART B: Check if a Number Belongs to the Sequence ---")
    
    # Input validation: Ensure number is a non-negative integer
    while True:
        try:
            num = int(input("Enter a number to check: "))
            if num >= 0:
                break
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
    # Iteratively generate numbers until we find or pass the target number
    a, b = 0, 1
    is_fibonacci = False
    
    while a <= num:
        if a == num:
            is_fibonacci = True
            break
        a, b = b, a + b
        
    # Print the appropriate message
    if is_fibonacci:
        print(f"{num} is a Fibonacci number.")
    else:
        print(f"{num} is NOT a Fibonacci number.")


def main():
    """Main function to control code workflow execution."""
    print_fibonacci_sequence()
    check_fibonacci_number()


if __name__ == "__main__":
    main()


