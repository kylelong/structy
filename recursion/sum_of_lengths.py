def sum_of_lengths(numbers):
    res = 0
    def backtrack(start, subset):
        nonlocal res
        arr = subset[:]
        res += sum(arr)
        subsets.append(arr)

        for i in range(start, len(numbers)):
            subset.append(numbers[i])
            backtrack(i + 1, subset)
            subset.pop()
            
    subsets = []
    backtrack(0, [])
    return res
        
print(sum_of_lengths([1,2,3,4]))