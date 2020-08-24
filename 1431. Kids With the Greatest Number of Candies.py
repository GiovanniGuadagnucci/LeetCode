candies = [2,3,5,1,3]
extraCandies = 3
resp = list()
for kid in candies:
    if kid + extraCandies >= max(candies):
        resp.append(True)
    else:
        resp.append(False)
print(list)
