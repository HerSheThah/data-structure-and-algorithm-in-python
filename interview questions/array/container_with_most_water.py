# Container With Most Water
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# max area between 8 and 7

def maxArea(height):
    maxarea=0
    i=0
    j=len(height)-1
    while i < j:
        maxarea = max(maxarea, min(height[i], height[j])*(j-i))
        if height[i]<height[j]:
            i+=1
        else:
            j-=1
    return maxarea

print(maxArea([2,3,4,5,18,17,6]))

# time --> o(n)
# space--> o(1)