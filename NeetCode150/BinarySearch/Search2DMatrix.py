def searchMatrix(matrix, target):
    t = 0 
    b = len(matrix) - 1
    while t < b:
        mid = (t + b) // 2 
        if matrix[mid][0] == target:
            return True
        elif matrix[mid][0] > target:
            b = mid + 1
        else:
            t = mid - 1
    l = 0
    r = len(matrix[0]) - 1 
    while l <= r:
        mid = (l + r) // 2
        if matrix[t][mid] == target:
            return True
        elif matrix[t][mid] > target:
            r -= 1
        else:
            l += 1
    return False