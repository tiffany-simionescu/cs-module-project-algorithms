'''
Input: a List of integers
Returns: a List of integers
'''
### Module 3 ###
# def product_of_all_other_numbers(arr):
#     # multiply all nums except for current index
#     # append the num to a new array

#     new_arr = []
#     # have 2 loops - one to keep track of current index
#     for i in range(0, len(arr)):
#         num = 1
#         # the other to keep track of the numbers in the list
#         for j in range(0, len(arr)):
#             if j != i:
#                 num *= arr[j]
#         new_arr.append(num)
    
#     return new_arr

### Module 4 ###
def product_of_all_other_numbers(arr):
    # multiply all nums except for current index
    # append the num to a new array
    num = 1
    for i in arr:
        num *= i
    # Take each index and divide the total product value 
    # of the array by the current index value 
    return [num / j for j in arr]

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
