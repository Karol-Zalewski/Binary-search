
"""
def binary_search(l, target, low= 0, high= None):
    Goes through the whole list l searching for the target.
    Implements binary search
    Args:
        l (list): list of words
        target (str): searched word


    
    lowest_possible_number = 0
    highest_possible_number = len(l)

    while highest_possible_number != lowest_possible_number:
        i = (highest_possible_number - lowest_possible_number)/2
        if l(i) < target:
            lowest_possible_number = i + 1
        elif l(i) > target:
            highest_possible_number = i
        else:
            return i
    return -1
    """'''
    if high == None:
        high = len(l) - 1
    if high < low:
        return -1
    midpoint = (low + high) // 2
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)
    else:
        return binary_search(l, target, midpoint + 1, high)

if __name__ == '__main__':
    sorted_list = set()
    length = 10000
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length, 3 * length))
    sorted_list = sorted(list(sorted_list))
    
    start = time.time()
    
    for target in sorted_list:
        naive_search(sorted_list, target)
    
    end = time.time()
    print('Naive search time: ', (end - start)/length, 'seconds')

    start = time.time()
    
    for target in sorted_list:
        binary_search(sorted_list, target)
    
    end = time.time()
    print('Binary search time: ', (end - start)/length, 'seconds')    
'''
import random
import time

def naive_search(l, target):
    """Goes through the whole list l searching for the target
    Args:
        l (list): list of values
        target (str): searched value
    """
    for i, value in enumerate(l):
        if value == target:
            return i
    return -1

def binary_search (l, target, lowest_value = 0, highest_value = None):
    """Employs binary search method to the list l searching for the target 
    Returns:
        The place of the searched value in the list or -1 if the target hasn't been found
    """
    if highest_value is None:
        highest_value = len(l)
    if highest_value >= lowest_value:
        mid_value = (highest_value + lowest_value) // 2

        if l[mid_value] > target:
            binary_search (l, target, lowest_value = lowest_value, highest_value = mid_value)
        elif l[mid_value] < target:
            binary_search (l, target, lowest_value = mid_value, highest_value = highest_value)
        elif l[mid_value] == target:
            return mid_value
    else:
        return -1
    
if __name__ == "__main__":
    sorted_list = set()
    
    for _ in range(0, 10000):
        sorted_list.add(random.randint(0, 100000))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for element in sorted_list:
        naive_search(sorted_list, element)
    end = time.time()

    print(f'Time required to perform naive search: {(end-start)/len(sorted_list)}')

    start = time.time()
    for element in sorted_list:
        binary_search(sorted_list, element)
    end = time.time()

    print(f'Time required to perform binary: {(end-start)/len(sorted_list)}')





