nums = [8, 1, 2, 2, 3]
cont = 0
valor = 0
ns = list()
for numero in nums:
    cont = 0
    valor = 0
    while cont < len(nums):
        if numero > nums[cont]:
            valor += 1
        cont += 1
    ns.append(int(valor))
print(ns)