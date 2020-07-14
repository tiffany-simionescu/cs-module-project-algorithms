'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # There will be a minimum len(arr) == 3
    if len(arr) < 3:
        return -1

    single_int = []
    # we want to loop over the arr and see if num is contained in arr twice
    for num in arr:
        # Add numbers to list
        if num not in single_int:
            single_int.append(num)
        # if the num exsists in the list, than remove the number already in the list
        else:
            single_int.remove(num)

    return single_int.pop()


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
    