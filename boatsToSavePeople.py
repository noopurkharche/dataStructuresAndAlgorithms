class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        
        left = 0
        right = len(people) - 1
        
        numOfBoats = 0
        while (left <= right):
            
            if people[left] + people[right] <= limit:
                left = left + 1
                right = right - 1
            else:
                right = right - 1
                
            numOfBoats = numOfBoats + 1
        return numOfBoats
