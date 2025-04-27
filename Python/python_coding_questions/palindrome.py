'''
Question: Detect Palindrome Substrings

Task: Write a Python function to find all substrings of a given string that are palindromes.
Example Input and Output:

    Input: "abba"
    Output: ["a", "b", "b", "a", "bb", "abba"]'''

def palindrome_substring(input_str):
    palindrome = []
    for i in range(len(input_str)+1):
        for j in range(i+1, len(input_str)+1):
            if input_str[i:j] == input_str[i:j][::-1]:
                palindrome.append(input_str[i:j])
    return palindrome


input_str = "abba"
output_list = palindrome_substring(input_str)
print(output_list)
