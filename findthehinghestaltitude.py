class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitudes = [0]
        for g in gain:
            altitudes.append(altitudes[-1] + g)
        return max(altitudes)