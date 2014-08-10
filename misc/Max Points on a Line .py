# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        max_counter = 0
        modifier = 0
        line = ()
        counter = {}

        if len(points) == 1:
            return 1
        if len(points) == 2:
            return 2

        for i in range(len(points)):
            for j in range(len(points)):
                if i == j: # this point, jump over
                    continue

                if points[i].x == points[j].x and points[i].y == points[j].y: # same point:
                    modifier += 1
                    continue

                elif points[i].x == points[j].x: # vertical
                    slope = -1
                    line = (i, slope)

                else: # not the same point
                    slope = float((points[i].y - points[j].y) / (points[i].x - points[j].x))
                    line = (i, slope)

                counter[line] = counter.get(line, 1) + 1

        max_counter = max(counter.values()) + modifier

        return max_counter

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

points = []
# lst = [(-4,-4),(-8,-582),(-3,3),(-9,-651),(9,591)]
lst = [(1,1),(1,1),(1,1),(1,2)]
for i in lst:
    point = Point()
    point.x, point.y = i
    points.append(point)

S = Solution()
print(S.maxPoints(points))