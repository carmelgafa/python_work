import operator

class Solution(object):
    
    def trap(self, height):

        right_idx = 0
        right_max = 0
        water_total = 0

        if len(height) > 0:
            curr_val = height[0]
            left_max = curr_val
            right_max = curr_val

            for i in range(1, len(height)-1):

                curr_val = height[i]

                if curr_val >= left_max:
                    left_max = curr_val

                if i >= right_idx:
                    sub_list = height[i:]
                    right_max = max(sub_list)
                    right_idx = sub_list.index(right_max)

                basin_depth = min(left_max, right_max) - curr_val

                if basin_depth > 0: 
                    water_total = water_total + basin_depth

                #print(f'{i}, {curr_val} --> {left_max}  -- {right_max}, {right_idx} -- {water_total}')

        return water_total

# height = []
height = [2,0,2]
height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [5,5,1,7,1,1,5,2,7,6]
sol = Solution()
print(sol.trap(height))