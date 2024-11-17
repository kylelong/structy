def most_frequent_char(s):
  counts = {}
  for c in s:
    counts[c] = counts.get(c, 0) + 1
    
  ans = None
  for c in s:
    if ans is None or counts[c] > counts[ans]:
      ans = c
  return ans
  