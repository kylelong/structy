def reverse(s):
    if s == '':
        return ''
    return s[-1] + reverse(s[:len(s) - 1])
assert reverse("kyle") == "elyk"
assert reverse("racecar") == "racecar"
assert reverse("") == ""
assert reverse("my name") == "eman ym"