def is_sorted(lst):
    """
    Check if a list is sorted.
    
    Parameters:
    lst (list): The list to check.
    
    Returns:
    bool: True if the list is sorted, False otherwise.
    """
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
