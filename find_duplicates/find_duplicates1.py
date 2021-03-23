def findDuplicates(nums):
        """
            Use extra space, a set, to track values already seen and return
            duplicates.

            :type nums: list
            :rtype: list  

            Time: O(n) where n is the number of values in num
            Space: O(n)         
        
        """
        
        seen = set()
        duplicates = [] 
        
        for i in range(len(nums)):
            if nums[i] in seen:
                duplicates.append(nums[i])
            else:
                seen.add(nums[i])
        return duplicates 