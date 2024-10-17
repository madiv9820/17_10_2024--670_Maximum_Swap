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