'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # There are n cookies in a jar
    # Cookie Monster can eat 1, 2, 3 cookies at a time
    # what are all the possibilities CM can eat the cookies?
        # if n = 3 then return answer 4:
        # 1. He can eat 1 cookie at a time 3 times
        # 2. He can eat 1 cookie, then 2 cookies 
        # 3. He can eat 2 cookies, then 1 cookie
        # 4. He can eat 3 cookies all at once.
        # Try Recursive with Fibanacci

    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")


# For Larger Input

# def eating_cookies(n, cache):
#     if n == 0:
#         return 1
#     elif n < 0:
#         return 0
#     elif cache[n] > 0:
#         return cache[n]
#     else:
#         cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
#         return cache[n]

# if __name__ == "__main__":
#     # Use the main function here to test out your implementation
#     num_cookies = 5
#     cashe = [0 for i in range(6)]

#     print(f"There are {eating_cookies(num_cookies, cache)} ways for Cookie Monster to each {num_cookies} cookies")
