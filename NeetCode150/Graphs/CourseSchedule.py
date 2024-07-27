"""
Medium: You are given an array prerequisites where pre[i] = [a, b] indicate that to take course a you must have taken course b.
Given the integer numCourses, indicating you must take course 0 - numCourse-1, return True if possible, else False.

Sol:
    - Given course A we must have done Course B, given Course B we must have done C etc...
    - This will only fail if we end up in a loop.
    - We do a DFS through the chain of courses until we reach the end, ie no prerequisite.
    - We can represent prerequisites for a course as a list [a, b, c] at the index in another list for the course.
    - An empty list will represent no prerequisite, hence if we reach [] then return True.
    - If we keep going and reach a course we have already looked at, return False.
"""

def canFinish(numCourses, prerequisites):
    visited = set() 
    pre = [[] for _ in range(numCourses)] 
    for a, b in prerequisites:
        pre[a].append(b)

    print("\nPre:", pre)

    def backtrack(i):
        print("Checking:", i, "Pre:", pre, "Visited:", visited)
        if i in visited:    # Found a loop
            print("  Loop")
            return False
        elif pre[i] is []:  # We have all prerequisites
            print("  Found all prerequisites")
            return True
        visited.add(i)
        for b in pre[i]:
            if not backtrack(b):
                return False
        visited.remove(i)
        pre[i] = []
        return True
        

    for a, b in prerequisites:
        if not backtrack(a):
            return False
    return True


def test():
    pre = [[1,0],[0,2],[2,1]]
    pre2 = [[0,1],[1,0]]
    pre3 = [[0,1],[0,2],[1,2]]
    print(canFinish(3, pre3))


test()