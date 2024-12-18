```
def three_sum(nums):
    # Sort the array first to help with processing
    nums.sort()
    result = []
    n = len(nums)

    # Iterate through the array
    for i in range(n - 2):
        # Skip duplicates to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # Use two-pointer technique
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                # Found a triplet that sums to zero
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move pointers
                left += 1
                right -= 1

            elif current_sum < 0:
                # Sum is too small, move left pointer to increase
                left += 1
            else:
                # Sum is too large, move right pointer to decrease
                right -= 1

    return result

# Example usage
arr = [-1, 0, 1, 2, -1, -4]
print(three_sum(arr))
```
