import re
string = 'Eu amo muito meu cachorro'
nstring = ''
for letra in string:
    if letra not in 'aeiouAEUIU':
        nstring += letra
print(nstring)