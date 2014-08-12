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
        cur_counter = 0
        modifier = {}
        counter = {}
        line = ()

        # if numbers of points is not enough, return directly
        if len(points) == 1:
            return 1
        if len(points) == 2:
            return 2

        # go through the list of points
        for i in range(len(points)):
            for j in range(len(points)):
                # this point, jump over
                if i == j:
                    continue

                # same point, calculate the modifier
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    modifier[i] = modifier.get(i, 1) + 1
                    continue

                # vertical, special process
                elif points[i].x == points[j].x:
                    slope = 'x'
                    line = (i, slope)

                # other cases, not the same point
                else:
                    slope = float((points[i].y - points[j].y)) / float((points[i].x - points[j].x))
                    line = (i, slope)

                # calculate the numbers of points on the same line
                counter[line] = counter.get(line, 0) + 1

            # if counter is NOT null, calculate normally
            if counter.values() != []:
                cur_counter = max(counter.values()) + modifier.get(i, 1)

            # if counter is NULL, calculate only the modifier
            else:
                cur_counter = modifier.get(i, 1)

            # if cur is bigger the max, set max to cur
            if cur_counter > max_counter:
                max_counter = cur_counter

            # clean the counter
            counter = {}

        return max_counter

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

points = []
# the case below has been passed, by changing float(A / B) to float(A) / float(B)
lst = [(84,250),(0,0),(1,0),(0,-70),(0,-70),(1,-1),(21,10),(42,90),(-42,-230)]

for i in lst:
    point = Point()
    point.x, point.y = i
    points.append(point)

S = Solution()
print(S.maxPoints(points))