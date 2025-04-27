'''
Question: Python Problem-Solving

Task: Write a Python function to find the longest substring in a given string that contains at most two distinct characters.
Example Input and Output:

    Input: "abcbbbbcccbdddadacb"
    Output: "bcbbbbcccb"'''


def longest_substring_with_two_distinct(s):
    # Dictionary to store character and its last seen index
    char_map = {}
    start = 0  # Left pointer of the window
    max_length = 0
    max_substring = ""

    # Expand the right pointer of the window
    for end in range(len(s)):
        char = s[end]
        char_map[char] = end  # Update the character's last seen position

        # If we have more than two distinct characters, shrink the window
        while len(char_map) > 2:
            # Find the leftmost character and remove it from the map
            leftmost_char = min(char_map, key=char_map.get)
            start = char_map[leftmost_char] + 1
            del char_map[leftmost_char]

        # Update the maximum length and substring if this window is longer
        if end - start + 1 > max_length:
            max_length = end - start + 1
            max_substring = s[start:end + 1]

    return max_substring

# Example usage
input_string = "abcbbbbcccbdddadacb"
result = longest_substring_with_two_distinct(input_string)
print(f"The longest substring with at most two distinct characters is: '{result}'")
