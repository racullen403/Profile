"""
Medium: Implement a simplified version of Twitter, allowing users to post tweets, follow/unfollow each other, and view the 10 most recent tweets 
within their own news feed.
"""
import heapq


class Twitter():

    def __init__(self):
        self.time = 0           # time for tracking latest tweets (-ve for minHeap)
        self.userTweets = {}    # Map of Person : [time, tweetId]  list
        self.userFollows = {}   # Map of Person : [followeeId] set

    
    def postTweet(self, userId, tweetId):
        self.follow(userId, userId)            # Ensures user exists
        if userId not in self.userTweets:      # If user doesnt exist, create them in tweets and add their [time, tweetId]
            self.userTweets[userId] = [] 
        self.userTweets[userId].append([self.time, tweetId])    # Add [time, tweet] to map and increment time
        self.time -= 1

    def follow(self, followerId, followeeId):
        if followerId not in self.userFollows :     # If user doesnt exist, create them and add their followee
            self.userFollows[followerId] = set()
        self.userFollows[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followerId == followeeId:                                # Dont unfollow self ever
            return
        if followerId in self.userFollows:                          # If follower exists
            if followeeId in self.userFollows[followerId]:          # And followee is in their list for following
                self.userFollows[followerId].remove(followeeId)     # Remove them from list
        
    def getNewsFeed(self, userId):
        follows = self.userFollows[userId]
        heap = []
        for p in follows:                                   # Create a minHeap for the most recent tweet from each followee 
            if p in self.userTweets:                        # this is more efficient then adding all tweets from everyone
                ind = len(self.userTweets[p]) - 1           # We track what tweet we are at my passing the index along
                time, tweetId = self.userTweets[p][ind]
                heap.append([time, tweetId, p, ind])
        heapq.heapify(heap)
        res = [] 
        while heap and len(res) < 10:                           # Keep popping, adding result, and placing next tweet into the heap
            time, tweetId, userId, ind = heapq.heappop(heap)
            res.append(tweetId)
            if ind > 0:
                time, tweetId = self.userTweets[userId][ind - 1]
                heapq.heappush(heap, [time, tweetId, userId, ind - 1])
        return res



