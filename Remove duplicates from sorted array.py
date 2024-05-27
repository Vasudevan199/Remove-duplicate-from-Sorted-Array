class Solution(object):
    @staticmethod
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        write_index = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[write_index] = nums[i]
                write_index += 1

        return write_index
if __name__ == '__main__':
    solution = Solution()  # Create an instance of the Solution class
    nums = [1, 1, 2]
    expectedNums = [1, 2]  # The expected array after removing duplicates

    k = solution.removeDuplicates(nums)  # Calls the removeDuplicates method on the instance

    # Verify the length
    assert k == len(expectedNums)
    
    # Verify the contents
    for i in range(k):
        assert nums[i] == expectedNums[i]

    print("All test cases passed.")
