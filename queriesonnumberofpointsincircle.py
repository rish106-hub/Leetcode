class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        for i, j, r in queries:
            ctr = 0
            for x, y in points:
                d = ((i-x)**2+(j-y)**2)**0.5
                if d<=r:
                    ctr+=1
            ans.append(ctr)
        return ans
        