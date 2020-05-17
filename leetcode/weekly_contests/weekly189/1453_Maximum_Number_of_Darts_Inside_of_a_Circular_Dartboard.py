from itertools import combinations
import math
class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        size = 10 ** 4
        res = 1
        if len(points) <= 0:
            return 0

        def Y_Coordinates(x, y, k, x0):
            return k * x0 - k * x + y;

    
        def getCenter(x1, y1, x2, y2):
            k = 0.0
            k_verticle = 0.0
            mid_x = 0.0
            mid_y = 0.0
            a = 1.0
            b = 1.0
            c = 1.0
            
            if caldist(x1, y1, (x1+x2)/2.0, (y1+y2)/2.0) > r ** 2:
                return []
            
            center = []
            if y2 - y1 == 0:
                center1x = (x1 + x2) / 2.0;
                center2x = (x1 + x2) / 2.0;
                center1y = y1 + sqrt(r * r -(x1 - x2) * (x1 - x2) / 4.0);
                center2y = y2 - sqrt(r * r -(x1 - x2) * (x1 - x2) / 4.0);
            else:
                if x2 - x1 == 0:
                    k_verticle = 0
                else:
                    k = (y2 - y1) / (x2 - x1)
                    k_verticle = -1.0 / k
                mid_x = (x1 + x2) / 2.0;
                mid_y = (y1 + y2) / 2.0;
                a = 1.0 + k_verticle * k_verticle;
                b = -2 * mid_x - k_verticle * k_verticle * (x1 + x2)
                c = mid_x * mid_x + k_verticle * k_verticle * (x1 + x2) * (x1 + x2) / 4.0 - \
                    (r * r - ((mid_x - x1) * (mid_x - x1) + (mid_y - y1) * (mid_y - y1)))

                # print(a, b,c, b * b -4 * a * c)
                center1x = (-1.0 * b + math.sqrt(b * b -4 * a * c)) / (2.0 * a)
                center2x = (-1.0 * b - math.sqrt(b * b -4 * a * c)) / (2.0 * a)
                center1y = Y_Coordinates(mid_x,mid_y,k_verticle,center1x)
                center2y = Y_Coordinates(mid_x,mid_y,k_verticle,center2x)
            return [[center1x, center1y], [center2x, center2y]]
        
        def caldist(x1, y1, x2, y2):
            dx = x2 - x1
            dy = y2 - y1
            return dx ** 2 + dy ** 2
                    
        for a, b in combinations(points, 2):
            mid = ((a[0] + b[0]) / 2.0, (a[1] + b[1]) / 2.0)
            centers = getCenter(a[0], a[1], b[0], b[1])
            for x, y in centers:
                if -size <= x <= size and -size <= y <= size:
                    count = 0
                    for p1, p2 in points:
                        if caldist(p1, p2, x, y) < r ** 2 + 1e-7:
                            count += 1
                    res = max(res, count)
                    
        return res
        