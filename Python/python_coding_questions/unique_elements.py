'''
Question 2: Data Structures

Write a Python function that takes a list of integers and returns 
a new list with only the unique elements, preserving their original order.'''

def unique(numbers):
    final = []
    seen = set()
    for num in numbers:
        if num not in seen:
            final.append(num)
            seen.add(num)
    return final


numbers_list = [2,4,5,6,78,4,3,4,5,6]
final_list = unique(numbers_list)
print(f"The final list is : {final_list}")