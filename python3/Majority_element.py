# Boyer - Moore Majority Voting Algorithm
# https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort() if you want to optimize in terms of memory
        temp = None
        count = 0

        for num in nums:
            if count == 0:
                temp = num
            count += 1 if num == temp else -1

        return temp