class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        for i in range(3, len(stones)):
            if stones[i] > (stones[i-1] * 2):
                return False

        stonePositions = set()
    
        for stone in stones:
            stonePositions.add(stone)
        #print(stonePositions)
    
        lastStone =  stones[len(stones) - 1]
    
        positions = []
        positions.append(0)
        jumps = []
        jumps.append(0)

        # in the following loop jumpDistance repressents k
        while len(positions) != 0:
            currentPosition = positions.pop()
            jumpDistance = jumps.pop()
            for i in range(jumpDistance - 1, jumpDistance + 2):
                if i <= 0:
                    continue
            
                nextPosition = currentPosition + i
            
                if nextPosition == lastStone:
                    return True
                elif nextPosition in stonePositions:
                    positions.append(nextPosition)
                    jumps.append(i)
        return False
 
