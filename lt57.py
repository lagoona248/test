class Solution:
    def insert(self, intervals, new_interval):
        uniting = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < new_interval[0]:
            uniting.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= new_interval[1]:
            new_interval = [min(intervals[i][0], new_interval[0]), max(intervals[i][1], new_interval[1])]
            i += 1

        uniting.append(new_interval)

        while i < n:
            uniting.append(intervals[i])
            i += 1

        return uniting


s = Solution()
intervals_1 = [[1, 3], [6, 9]]
newInterval_1 = [2, 5]
intervals_2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval_2 = [4, 8]
print("first:", s.insert(intervals_1, newInterval_1))
print("second:", s.insert(intervals_2, newInterval_2))
