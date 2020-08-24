nums = [1,2,3,4]
nnums = list()
c = 1
for value in nums:
    soma = sum(nums[:c])
    c+=1
    nnums.append(soma)
print(nnums)