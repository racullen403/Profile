import math

def minEatingSpeed(piles, h):
    smallest = 1 
    largest = max(piles)
    least = max(piles)
    while smallest < largest:
        time = 0
        k = (largest + smallest) // 2
        for p in piles:
            # while p > 0:
            #     time += 1 
            #     p -= k     Too slow for test cases
            time += math.ceil(float(p)/k)
        if time <= h:
            least = k
            largest = k - 1
        else:
            smallest = k + 1
    return least

def test():
    a = [1,4,3,2]
    b = 9 
    print(minEatingSpeed(a, b))

test()
        