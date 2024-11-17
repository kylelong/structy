def max_value(nums):
  res = float("-inf")
  for n in nums:
    if n > res:
      res = n
  return res