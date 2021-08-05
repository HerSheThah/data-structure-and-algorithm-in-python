
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6


# METHOD 1 BRUT FORCE
# def max_element(start, end , arr):
#     high=0
#     for i in range(start, end+1):
#         if arr[i]> high:
#             high=arr[i]
#     return high
#
# def trap(height):
#     total_water =0
#     for i in range(len(height)):
#         l=max_element(0, i, arr)
#         r=max_element(i,len(height)-1, arr)
#         total_water += min(l, r)-arr[i]
#     return total_water

# time --> o(n^2)
# space --> o(1)

# ============================================================================================
# METHOD 2

# def trap(height):
#     n=len(height)
#     l_arr=[None]*n
#     r_arr=[None]*n
#     total=0
#     l_arr[0]=height[0]
#     r_arr[n-1]=height[n-1]
#
#     for i in range(1, n):
#         l_arr[i]= max(l_arr[i-1], height[i])
#
#     for i in range(n-2,-1, -1):
#         r_arr[i]=max(r_arr[i+1],height[i])
#
#     for i in range(n):
#         total += min(l_arr[i], r_arr[i])-height[i]
#
#     print(total)

# time --> o(n)
# space --> o(n)

# ============================================================================================
# METHOD 3
def trap(height):
    n=len(height)
    l_max=0
    r_max=0
    l=0
    r=n-1
    total=0
    while l<=r:
        if r_max<=l_max:
            total += max(0, r_max-height[r])
            r_max=max(r_max, height[r])
            r-=1
        else:
            total += max(0, l_max-height[l])
            l_max=max(l_max, height[l])
            l+=1
    print(total)

# time --> o(n)
# space -->o(1)

arr=[4,2,0,3,2,5]
trap(arr)