class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

    # Initialize a deque to store indices of elements in the current window
        window = deque()

        result = []  # To store the maximum values for each window

        # Iterate through the array
        for i in range(len(nums)):
            # Remove elements that are out of the current window from the front of the deque
            while window and window[0] < i - k + 1:
                window.popleft()

            # Remove elements that are less than the current element from the back of the deque
            while window and nums[window[-1]] < nums[i]:
                window.pop()

            # Add the current index to the deque
            window.append(i)

            # The front of the deque contains the maximum element in the current window
            if i >= k - 1:
                result.append(nums[window[0]])

        return result