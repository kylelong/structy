def anagrams(s1, s2):
  return counts(s1) == counts(s2)
  
def counts(s):
  freq = {}
  for c in s:
    freq[c] = freq.get(c, 0) + 1
  return freq



    
  