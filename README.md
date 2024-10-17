## Brute Force Solution

- ### Intuition
    - To maximize the number by swapping two digits, we need to identify the first digit that can be exchanged with a larger digit to its right.

- ### Step-by-Step Approach
    1. **Convert the number to a list of digits** for easier manipulation.
    2. **Iterate through each digit** (except the last one) to identify potential swap candidates.
    3. For each digit, **check subsequent digits** to find the largest digit that is greater than the current digit.
    4. If a larger digit is found, **swap them** and break out of the loop to maximize the number immediately.
    5. **Convert the list back to an integer** and return the result.

- ### Time Complexity
    - ___O(n²)___: The outer loop iterates through each digit, while the inner loop searches for a larger digit among the subsequent digits, resulting in a quadratic time complexity.

- ### Space Complexity
    - ___O(n)___: The algorithm requires additional space to store the list of digits, which is proportional to the number of digits in the input number.

- ### Code
    ```python
    class Solution:
        def maximumSwap(self, num: int) -> int:
            # Convert the integer to a string to access each digit
            num_str = str(num)
            digits = [int(digit) for digit in num_str]
            n = len(digits)  # Number of digits

            # Iterate through each digit except the last one
            for current_index in range(n - 1):
                max_digit_index = -1  # Initialize index for the maximum digit
                max_digit = -1  # Initialize maximum digit found

                # Check subsequent digits for a larger digit to swap
                for next_index in range(current_index + 1, n):
                    if (digits[next_index] > digits[current_index] and
                            digits[next_index] >= max_digit):
                        max_digit = digits[next_index]
                        max_digit_index = next_index

                # Swap if a larger digit is found
                if max_digit_index != -1:
                    digits[current_index], digits[max_digit_index] = digits[max_digit_index], digits[current_index]
                    break  # Exit after the first swap

            # Convert back to integer and return
            return int(''.join(str(digit) for digit in digits))
    ```