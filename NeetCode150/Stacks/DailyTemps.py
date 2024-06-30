def dailyTemperatures(temps):
    # Medium: We need to keep track of the indices of the temps in a stack. If we reach a temperature 
    # larger than the most recent in the stack, then start popping all items until we find a day with 
    # same or higher temp. Each time we pop, update the index with the distance between the recent 
    # temp and the temp that was popped.
    stack = []
    res = [0] * len(temps)
    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            index = stack.pop()
            res[index] = i - index
        stack.append(i)
    return res 


        
