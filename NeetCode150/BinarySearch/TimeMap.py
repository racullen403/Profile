class TimeMap:

    def __init__(self):
        self.lookup = {}

    def set(self, key, value, timestamp):
        if key not in self.lookup:
            self.lookup[key] = []
        self.lookup[key].append([value, timestamp])
    
    def get(self, key, timestamp):
        res = ""
        arr = self.lookup.get(key, [])
        l = 0
        r = len(arr) - 1
        while l <= r:
            m = (l + r)//2
            if timestamp >= arr[m][1]:
                res = arr[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
            

        