def findDuplicates(nums):
        """
            Mark a visited number as negative and append to result 
            when encountered again.

            :type nums: list
            :rtype: list        
            
            Time: O(n) where n is the number of values in nums
            Space: O(1)

        """
        duplicates = []

        if len(nums) == 1:
            return ret
        
        for i in range(len(nums)):
            if nums[i] < 0:
                if nums[(-1*nums[i])-1] > 0:
                    nums[(-1*nums[i])-1] *= -1
                else:
                    duplicates.append((-1*nums[i]))
            else:
                if nums[nums[i]-1]<0:
                    duplicates.append(nums[i])
                else:
                    nums[nums[i]-1] *= -1
        return ret