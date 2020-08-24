nums = [1, 2, 3, 1, 1, 3]
resp = 0
contados = list()
for n in nums:
    if n in contados:
        print(f'{n} já foi contado')
    else:
        cont = nums.count(n)
        resp += cont*(cont-1)//2
        contados.append(n)
return resp
