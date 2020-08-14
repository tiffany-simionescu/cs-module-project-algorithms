'''
Input: a List of integers
Returns: a List of integers
'''
### Module 3 and Module 4 ###
def moving_zeroes(arr):
    # 0s need to be on the right
    # all other nums on the left

    # Create two arrays - one for 0s and one for other nums
    new_arr = []
    zero_arr = []

    # loop through array
    for num in arr:
        if num == 0:
            zero_arr.append(num)
        else:
            new_arr.append(num)
    # return arr1 + arr2
    return new_arr + zero_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")