H = [0,1,0,2,1,0,1,3,2,1,2,1]
n = len(H)
# max of left
maxl = 0
# max of right
maxr = 0
left = 0
right = n-1
water = 0

while left < right:
    if H[left] < H[right]:
        if H[left] >= maxl:
            maxl = H[left]
        else:
            water = water + ( maxl - H[left])
        left = left + 1 
    else:
        if H[right] >= maxr:
            maxr = H[right]
        else:
            water = water + (maxr - H[right])
        right = right - 1
        
print("Trapped Water = " + str(water))
