s = "aaiougrt"
indices = [4,0,2,6,7,3,1,5]
ns = ['']*len(s)
for indice, numeros in enumerate(indices):
    ns[numeros] = s[indice]
return ''.join(ns)