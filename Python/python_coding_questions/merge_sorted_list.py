'''
Question: Merge Two Sorted Lists

Task: Write a Python function to merge two sorted lists into one sorted list.
Example Input and Output:

    Input:

list1 = [1, 3, 5]
list2 = [2, 4, 6]

Output:

    [1, 2, 3, 4, 5, 6]

Requirements:

    The function should handle lists of different lengths.
    Avoid using built-in sorting functions (sorted() or .sort()).

Would you like to attempt this, or should I provide the solution? 😊'''

def merge_lists(list1, list2):
    i,j = 0,0
    merged = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1 
    print(merged)  
    while i < len(list1):
        merged.append(list1[i])
        i += 1               

    while j < len(list2):
        merged.append(list2[j])
        j += 1 
    return merged

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6]
merged_list = merge_lists(list1, list2)
print(merged_list)

        

