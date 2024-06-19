"""
Shell Sort:

    This is a generalisation of the Insertion Sort. It first sorts elements that are far apart, and successively
    reduces the interval between the elements to be sorted.

    The interval between elements is reduced based on some chosen sequence,

        Shells Original: N/2,  N/4, N/8, ..., 1

    The performance of a Shell Sort is dependent on the input array and the sequence used.


    E.G.    Take input [9, 8, 3, 7, 5, 6, 4, 1] and we will use the original Shell sequence.


                First with N/2 = 8/2 = 4

                    We apply the insertion sort method to elements that are 4 spaces apart.

                    - Starting [9, 8, 3, 7, 5, 6, 4, 1], apply on 9, 5    [5, 8, 3, 7, 9, 6, 4, 1]
                                |           |

                    - Next [5, 8, 3, 7, 9, 6, 4, 1] apply on 8, 6    [5, 6, 3, 7, 9, 8, 4, 1]
                               |           |

                    - Next [5, 6, 3, 7, 9, 8, 4, 1] apply on 3, 4    [5, 6, 3, 7, 9, 8, 4, 1]
                                  |           |

                    - Finally  [5, 6, 3, 7, 9, 8, 4, 1]  apply on 7, 1   [5, 6, 3, 1, 9, 8, 4, 7]
                                         |           |


                Second with N/4 = 8/4 = 2

                    - [5, 6, 3, 1, 9, 8, 4, 7]  apply 5, 3    [3, 6, 5, 1, 9, 8, 4, 7]
                       |     |

                    - [3, 6, 5, 1, 9, 8, 4, 7]  apply 6, 1    [3, 1, 5, 6, 9, 8, 4, 7]
                          |     |

                    - This is where there is a slight change, all elements in the interval, up to the current
                    position must be compared

                      [3, 6, 5, 1, 9, 8, 4, 7] apply 3, 5, 9    [3, 6, 5, 1, 9, 8, 4, 7]
                       |     |     |

                    - [3, 6, 5, 1, 9, 8, 4, 7] apply 6, 1, 8    [1, 6, 5, 3, 9, 8, 4, 7]
                          |     |     |

                    - [3, 6, 5, 1, 9, 8, 4, 7] apply 3, 5, 9, 4  [3, 6, 4, 1, 5, 8, 9, 7]
                       |     |     |     |

                    - [3, 6, 4, 1, 5, 8, 9, 7] apply 6, 1, 8, 7   [3, 1, 4, 6, 5, 7, 9, 8]
                          |     |     |     |


                Finally we apply on N/8 = 8/7 = 1, this is just a normal insertion sort and will create the final
                sorted array.

                    [3, 1, 4, 6, 5, 7, 9, 8]

                    - [3, 1, 4, 6, 5, 7, 9, 8]   becomes  [1, 3, 4, 6, 5, 7, 9, 8]
                       |  |

                    - [1, 3, 4, 6, 5, 7, 9, 8]  becomes   [1, 3, 4, 6, 5, 7, 9, 8]
                       |  |  |

                    - [1, 3, 4, 6, 5, 7, 9, 8]  becomes   [1, 3, 4, 6, 5, 7, 9, 8]
                       |  |  |  |

                    - [1, 3, 4, 6, 5, 7, 9, 8] becomes   [1, 3, 4, 5, 6, 7, 9, 8]
                       |  |  |  |  |

                    - [1, 3, 4, 5, 6, 7, 9, 8] becomes   [1, 3, 4, 5, 6, 7, 9, 8]
                       |  |  |  |  |  |

                    - [1, 3, 4, 5, 6, 7, 9, 8] becomes   [1, 3, 4, 5, 6, 7, 9, 8]
                       |  |  |  |  |  |  |

                    - [1, 3, 4, 5, 6, 7, 9, 8] becomes   [1, 3, 4, 5, 6, 7, 8, 9]
                       |  |  |  |  |  |  |  |


                Sequence is done so array sorted.


Shell sort does not compare objects between the intervals and so is not Stable

Time Complexity:
    Average case is O(nlogn), it really depends on the interval sequence.

Space Complexity:
    Everything is done in place, O(1)

"""


# Shell sort using original N/2, N/4, ..., 1 sequence
def shell_sort(arr):
    n = len(arr)
    n //= 2
    while n > 0:  # This loops through our Shell Sequence given by n
        for i in range(n, len(arr)):  # Finds the last index of current interval
            temp = arr[i]
            while (i - n) >= 0 and temp < arr[i - n]:
                arr[i] = arr[i - n]
                i -= n
            arr[i] = temp
        n //= 2


def shell_sort_show(arr):
    n = len(arr)
    n //= 2
    while n > 0:
        print("\nStarting Arr:", arr)
        print("Interval:", n)
        for i in range(n, len(arr)):
            temp = arr[i]
            print("\n    Temp:", temp)
            while (i - n) >= 0 and temp < arr[i - n]:
                arr[i] = arr[i - n]
                print("    Swap:", arr)
                i -= n
            arr[i] = temp
            print("    Insert:", arr)
        n //= 2
    print("\nSorted Array:", arr)


def example1():
    a = [9, 8, 3, 7, 5, 6, 4, 1]
    shell_sort_show(a)



