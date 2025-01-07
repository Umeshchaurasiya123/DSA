def product_except_self(nums):
    n = len(nums)
    memo = {}

    def helper(index, direction):
        # Base case: when index is out of bounds
        if index < 0 or index >= n:
            return 1

        # Check if already computed
        if (index, direction) in memo:
            return memo[(index, direction)]

        # Recursive case: calculate product based on direction
        if direction == "left":
            result = helper(index - 1, direction) * nums[index]
        else:  # direction == "right"
            result = helper(index + 1, direction) * nums[index]

        memo[(index, direction)] = result
        return result

    # Compute left and right products
    left_products = [helper(i - 1, "left") for i in range(n)]
    right_products = [helper(i + 1, "right") for i in range(n)]

    # Calculate final result
    ans = [left_products[i] * right_products[i] for i in range(n)]
    return ans

# Test the function
nums = [1, 2, 3, 4]
print(product_except_self(nums))


