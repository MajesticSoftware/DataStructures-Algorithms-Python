def reverse(nums):

    #pointing to the first item
    start_index = 0

    # index point to back
    end_index = len(nums)-1

    while end_index > start_index:
        #Keep swapping the items
        nums[end_index], nums[start_index] = nums[start_index], nums[end_index]
        start_index += 1
        end_index -= 1

if __name__ == '__main__':
    n = [-3,0,3]
    reverse(n)
    print(n)