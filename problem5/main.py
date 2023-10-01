def max_sequence(arr):
    if not arr:
        return 0
    max_temp = max_arr = arr[0]
    
    for i in range (1, len(arr)):
        max_temp = max(arr[i], max_temp + arr[i])
        max_arr = max(max_arr, max_temp)
        
    return max_arr
        
if __name__ == "__main__":
    print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(max_sequence([-2, -5, 6, -2, -3, 1, 5, -6]))    # 7
    print(max_sequence([-2, -3, 4, -1, -2, 1, 5, -3]))    # 7
    print(max_sequence([-2, -5, 6, -2, -3, 1, 6, -6]))    # 8
    print(max_sequence([-2, -5, 6, 2, -3, 1, 6, -6]))     # 12