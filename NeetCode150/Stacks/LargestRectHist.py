def largestRectangleArea(heights):
    stack = [] 
    area = 0
    for i, h in enumerate(heights):
        start = i
        while stack and h < stack[-1][1]:
            index, height = stack.pop()
            area = max(area, height * (i - index))
            start = index
        stack.append((start, h))
    for i, h in stack:
        area = max(area, h * (len(heights) - i))
    return area


