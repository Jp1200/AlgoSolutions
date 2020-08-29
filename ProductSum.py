def productSum(array, depth=1):
    ans = 0

    for item in array:
        if type(item) is list:
            ans += productSum(item, depth + 1)
        else:
            ans += item
    return ans * depth
