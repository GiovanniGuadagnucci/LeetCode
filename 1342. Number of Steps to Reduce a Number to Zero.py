num = 14
fim = num
resposta = 0

while fim != 0:
    if fim % 2 == 0:
        fim = fim / 2
        resposta += 1
    else:
        fim -= 1
        resposta += 1
print(resposta)
return resposta
