S = "aAAbbbb"
J = "aA"
count = 0
for stone in S:
    if stone in J:
        count += 1
return count