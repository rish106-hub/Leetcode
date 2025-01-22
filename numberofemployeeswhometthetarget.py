class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        ctr=0
        for i in range(len(hours)):
            if(hours[i]>=target):
                ctr+=1
        return ctr
        