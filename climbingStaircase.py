# climbing staircase recursive
# can take one step or two steps

def climbingStaircase(n):
    
    if n < 0:
        return 0
    
    if n == 0:
        return 1
        
    val1 = climbingStaircase(n-1)
    val2 = climbingStaircase(n-2)
    
    return val1 + val2


print(climbingStaircase(4))
