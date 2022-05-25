def reverse_int(integer):
    integer = str(integer)
    integer = list(integer)

    # pointing to the first item
    start_index = 0

    # index point to back
    end_index = len(integer) - 1

    while end_index > start_index:
        # Keep swapping the items
        integer[end_index], integer[start_index] = integer[start_index], integer[end_index]
        start_index += 1
        end_index -= 1
    integer = "".join(integer)
    return int(integer)

if __name__ == '__main__':
    print(reverse_int(1234))