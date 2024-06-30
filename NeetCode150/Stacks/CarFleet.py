def carFleet(target, position, speed):
    # Medium: Actually quite hard. Sort the cars into reverse order. Have a stack that holds the fleet 
    # of cars. Then iterating through cars, work out how long it would take said car to reach destination.
    # If this is faster than slower than previous car in stack, that car will catch up and be part of the 
    # fleet, so pop it, continue until stack is empty or no car can reach fleet, then push into stack.
    # At the end, the length of the stack will give us the number of fleets.
    cars = list(zip(position, speed))
    cars.sort(reverse = True, key= lambda x : x[0])
    fleet = []
    while cars:
        car = cars.pop() 
        t = (target - car[0]) / car[1]
        while fleet and fleet[-1] <= t:
            fleet.pop()
        fleet.append(t)
    return len(fleet)

