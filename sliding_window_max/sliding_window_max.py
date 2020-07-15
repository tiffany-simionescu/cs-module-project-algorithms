'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # k is the size of the window/list
    # it moves right by 1 index and will hold k amounts of indexes
    # find the greater number
    # append the greater number to a new list
    # if k is greater than the len of nums, return -1

    new_arr = []
    start = 0
    end = k

    if end > len(nums):
        return -1

    while end <= len(nums):
        greater_num = nums[start]
        for i in range(start + 1, end):
            if nums[i] > greater_num:
                greater_num = nums[i]
        new_arr.append(greater_num)
        start += 1
        end += 1

    return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
