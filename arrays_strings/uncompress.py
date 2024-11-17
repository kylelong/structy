import string
def uncompress(s):
  lowercase = string.ascii_lowercase
  num, res = '', ''
  for c in s:
    if c not in lowercase:
      num += c
    else:
      factor = int(num)
      res += factor * c
      num = ''
  return res
      
      
      