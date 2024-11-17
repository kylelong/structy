def compress(s):
  s += '!'
  i, j = 0, 0
  res = []
  while j < len(s):
    if s[i] == s[j]:
      j += 1
    else:
      count = j - i
      if count == 1:
        res.append(s[i])
      else:
        res.append(str(count))
        res.append(s[i])
      i = j
  return ''.join(res)
 