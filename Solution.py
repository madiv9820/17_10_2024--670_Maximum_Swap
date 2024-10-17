class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the integer to a string to easily access each digit
        num_str = str(num)
        # Create a list of digits as integers
        digits = [int(digit) for digit in num_str]
        n = len(digits)  # Get the number of digits

        # Iterate through each digit except the last one
        for current_index in range(n - 1):
            max_digit_index = -1  # Initialize index of the maximum digit to swap with
            max_digit = -1  # Initialize the maximum digit found to swap

            # Check all subsequent digits to find a larger digit for swapping
            for next_index in range(current_index + 1, n):
                # If a larger digit is found, update max_digit and its index
                if (digits[next_index] > digits[current_index]
                        and digits[next_index] >= max_digit):
                    max_digit = digits[next_index]
                    max_digit_index = next_index

            # If a valid maximum digit is found for swapping
            if max_digit_index != -1:
                # Swap the current digit with the found maximum digit
                digits[current_index], digits[max_digit_index] = digits[max_digit_index], digits[current_index]
                break  # Exit after the first swap to maximize the number

        # Convert the list of digits back to an integer and return it
        return int(''.join(str(digit) for digit in digits))

# Time complexity: O(n^2), where n is the number of digits in the input number.
# Space complexity: O(n), for storing the list of digits.