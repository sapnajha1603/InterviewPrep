'''
Question: Reverse Words in a Sentence

Task: Write a Python function to reverse the words in a given sentence while keeping the order of words intact.
Example Input and Output:

    Input: "Hello World from Python"
    Output: "olleH dlroW morf nohtyP"

Requirements:

    Only the words themselves should be reversed.
    The order of the words in the sentence must remain the same.

Would you like to try this or see the solution? 😊'''

def reverse_word(input_str):
    input_list = input_str.split()
    reverse_list = []
    for inp in input_list:
        reverse_list.append(inp[::-1])
    return " ".join(reverse_list)
input_str = "Hello World from Python"
reverse_op = reverse_word(input_str)
print(reverse_op)

