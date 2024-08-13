def binarySort(arr, number_to_find):
    left_index=0
    right_index=len(arr)-1
    mid_index=0

    while left_index <= right_index:
        mid_index=(left_index+right_index) // 2
        mid_number=arr[mid_index]
        if mid_number == number_to_find:
            return mid_index
        elif mid_number > number_to_find:
            right_index = mid_index-1
        else :
            left_index = mid_index + 1

    return -1
arr=[2,55,73,223,45,67]
arr.sort()
index=binarySort(arr, 67)
print(index)