"""Functions that implement sorting algorithms."""

__author__ = "730671723"

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    for i in range(1, len(x)):  
        val = x[i]  
        j = i-1
        while j >= 0 and val < x[j]:  
            x[j+1] = x[j]  
            j -= 1
        x[j+1] = val  
  
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    for ind in range(len(x)):
        smallnum=ind
        for j in range(ind + 1, len(x)):
            if x[j] < x[smallnum]:
                smallnum = j
        (x[ind], x[smallnum]) = (x[smallnum], x[ind])
    return None
    