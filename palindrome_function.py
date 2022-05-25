
#it has 0(s) so basically linear tunning time complexity as far as number
# of letters in the string is concerned.

def is_palindrome(s):
    original_string = s
    # this is what we have implemented in previous lecture in O(N)
    reverse_string = reverse(s)
    if original_string == reverse_string:
        return True
    return False


def reverse(data):
    #Convert data into list
    data = list(data)
    # pointing to the first item
    start_index = 0

    # index point to back
    end_index = len(data) - 1

    while end_index > start_index:
        # Keep swapping the items
        data[end_index], data[start_index] = data[start_index], data[end_index]
        start_index += 1
        end_index -= 1
    return "".join(data)

def palindrome_python(s):
    if s == s[::-1]:
        return True
    return False


if __name__ == '__main__':
    test_array = [1,2,3,4,5,6,7,8,9]
    print(is_palindrome("racecar"))
    print(reverse("Hello"))
