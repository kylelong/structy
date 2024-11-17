def pair_sum(numbers, target_sum):
  previous = {}
  
  for idx, num in enumerate(numbers):
    compliment = target_sum - num
    if compliment in previous:
      return (previous[compliment], idx)
    previous[num] = idx
    