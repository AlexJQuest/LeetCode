from collections import Counter
class Solution:
    def compress(self, chars: List[str]) -> int:
        # Initialize pointers
        read_ptr = 0
        write_ptr = 0

        # Iterate through the array
        while read_ptr < len(chars):
            # Current character
            current_char = chars[read_ptr]
            # Count consecutive characters
            count = 0
            while read_ptr < len(chars) and chars[read_ptr] == current_char:
                read_ptr += 1
                count += 1
            # Write compressed character to the array
            chars[write_ptr] = current_char
            write_ptr += 1
            # If count is greater than 1, write its digits to the array
            if count > 1:
                count_str = str(count)
                for digit in count_str:
                    chars[write_ptr] = digit
                    write_ptr += 1

        return write_ptr