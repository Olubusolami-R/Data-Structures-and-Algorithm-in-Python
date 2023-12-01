class Solution:
    def moveZeroes(self, nums: list[int]) -> None:

        zero_ptr=0
        non_zero_ptr=1

        while non_zero_ptr!=len(nums):
            if nums[zero_ptr]==0:
                if nums[non_zero_ptr]!=0:
                    nums[zero_ptr],nums[non_zero_ptr]=nums[non_zero_ptr],nums[zero_ptr]
                    zero_ptr+=1
                    non_zero_ptr+=1
                else:
                    non_zero_ptr+=1
            else:
                if nums[non_zero_ptr]!=0:
                    non_zero_ptr+=1
                zero_ptr+=1

#Btw amazing runtime and memory! Way to go!
#A much simpler way would be to simply have a pointer, 
#iterate through the array and everytime you find a non-zero val put it at the beginning and increment the counter. 
#Then fill the rest of the array from count till len(nums)-1 with 0s.