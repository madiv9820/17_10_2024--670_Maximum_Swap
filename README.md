## Greedy Approach

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