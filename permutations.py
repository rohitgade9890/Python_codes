#genrate all permutations of list and strings
def permutations(arr):
    # Base case: only one element
    
    if len(arr) == 1:
        return [arr[:]]
    
    result = []
    for i in range(len(arr)):
        # pick element at index i
        current = arr[i]
        # remaining elements
        remaining = arr[:i] + arr[i+1:]
        # get permutations of remaining
        for p in permutations(remaining):
            result.append([current] + p)
    
    return result

# Example
arr = [1, 2, 3]
print(permutations(arr))

def string_permutations(s):
    s = ''.join(sorted(s))   # ensure lexicographic order
    if len(s) == 1:
        return [s]
    
    result = []
    for i in range(len(s)):
        current = s[i]
        remaining = s[:i] + s[i+1:]
        for p in string_permutations(remaining):
            result.append(current + p)
    return result

# Example
s = "abc"
print(string_permutations(s))

