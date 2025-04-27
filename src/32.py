def find_min_max(lst):
    min_val = max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
        elif num < min_val:
            min_val = num
    return min_val, max_val

# Example usage:
numbers = [12, 34, -56, 78, -90]
print(find_min_max(numbers))  # Output: (-56, 78)
