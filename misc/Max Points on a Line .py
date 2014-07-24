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
        cur_coutner = 2
        k_init = None
        k_curr = None

        if len(points) == 1:
            return 1
        if len(points) == 2:
            return 2

        for i in range(len(points)):
            for j in range(len(points))[i+1:]:
                if points[i].x == points[j].x and points[i].y == points[j].y: # same point:
                    cur_coutner += 1
                    continue
                else: # not same point
                    if k_init == None: # get first k
                        if points[i].x - points[j].x == 0: # horizontal
                            k_init = -1
                        else: # normal
                            k_init = (points[i].y - points[j].y) / (points[i].x - points[j].x)
                    else: # current k
                        if points[i].x - points[j].x == 0: # horizontal
                            k_init = -1
                        else: # normal
                            k_init = (points[i].y - points[j].y) / (points[i].x - points[j].x)

                if k_curr == k_init:
                    cur_coutner += 1

            if cur_coutner > max_counter:
                max_counter = cur_coutner
            cur_coutner = 2
            k_init = None

        return max_counter

S = Solution()
S.maxPoints([(0,0),(1,1),(1,-1)])