# Maximum Swap: Brute Force and Optimized Greedy Approaches

- ## Brute Force Solution

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

- ## Greedy Approach

    - ### Intuition
        - The goal is to maximize the number by swapping two digits. The optimal strategy is to find the first digit that can be exchanged with a larger digit that appears later in the number. This ensures that the resulting number is as large as possible.

    - ## Approach
        1. **Convert the number to a list of digits** for easier manipulation.
        2. **Create an array to track the last occurrence** of each digit (0-9).
        3. **Iterate through the digits**:
            - For each digit, check for larger digits (from 9 down to the current digit).
            - If a larger digit exists later in the number, perform the swap and return the result immediately.
        4. If no swap is made, return the original number.

    - ### Time Complexity
        - ___O(n)___: The algorithm processes the digits in linear time. It first fills the last occurrence array in O(n) and then checks for swaps in O(n), resulting in an overall linear complexity.

    - ### Space Complexity
        - ___O(1)___: The space complexity is constant because the `last` array has a fixed size of 10, regardless of the number of digits in the input number.

    - ### Code
        ```python
        class Solution:
            def maximumSwap(self, num: int) -> int:
                # Convert the number to a list of digits
                digits = [int(digit) for digit in str(num)]
                last = [0] * 10  # Array to store the last occurrence of each digit

                # Fill the last occurrence array
                for i, digit in enumerate(digits):
                    last[digit] = i

                # Iterate through the digits
                for i in range(len(digits)):
                    # Check for a larger digit to swap with
                    for d in range(9, digits[i], -1):
                        if last[d] > i:  # If a larger digit exists later
                            # Perform the swap
                            digits[i], digits[last[d]] = digits[last[d]], digits[i]
                            return int(''.join(map(str, digits)))  # Return the result immediately

                return num  # Return the original number if no swap was made
        ```