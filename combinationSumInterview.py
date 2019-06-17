# S is the sum, N be number of rolls. Find out the combinations which would lead to S Sum in N rolls
# s = 12
# n = 3
# output = [[2,4,6],[1,1,10],[1,3,8].....]
    
def dfs(candidates,index,path,target,res,n):
    
    if target < 0:
        return
    
    if n < 0:
        return
    
    if target == 0 and n == 0:
        #remove duplicates
        path.sort()
        if path not in res:
            res.append(path)
        return
    
    for i in range(index,len(candidates)):
        dfs(candidates,index,path + [candidates[i]],target - candidates[i],res, n-1)
        
        
        
res = []
sum = 12
n = 3
candidates = [x for x in range(1,sum)]
print(candidates)
candidates.sort()
dfs(candidates,0,[],sum,res,n)

print(res)

