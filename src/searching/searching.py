# TO-DO: Implement a recursive implementation of binary search
l = [1, 2, 3, 4, 7]


def binary_search(arr, target, start, end):
    # Your code here
    # The idea is to divide the array into lower and higher parts
    # The lower elements will be on the left of our target and the elements with higher value will be on the right
    # We divide the list into 3, the middle, the left, and
    # If target < middle, we forget the right hand side and focus on the left and vice versa
    middle = (start+end)/2
    if target == arr[middle]:
        return
    if target > arr[middle]:
        RHS = arr[middle+1:]
        binary_search(RHS, target, [middle+1], end)
    else:
        LHS = arr[:middle]
        binary_search(LHS, target, start, [middle-1])

        # STRETCH: implement an order-agnostic binary search
        # This version of binary search should correctly find
        # the target regardless of whether the input array is
        # sorted in ascending order or in descending order
        # You can implement this function either recursively
        # or iteratively


# def agnostic_binary_search(arr, target):
    # Your code here
