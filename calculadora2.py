ListadeUnidades= ['bit','byte','KB','MB','GB','TB','PB']
Unidadeinicial= input ("Insira a unidade inicial: ")
UnidadeFinal= input ("Insira a unidade final: ")
Valor= int(input ("Insira o valor a ser convertido:"))
posiçãoinicial= 0
posiçãofinal= 0
unidadebit= 'bit'

if Unidadeinicial == unidadebit:
        Valor3 = Valor / 8
        Unidadeinicial = "byte"
else:
        Valor3 = Valor

for i in ListadeUnidades:
        if i == Unidadeinicial:
                posiçãoinicial=ListadeUnidades.index(i)
        if i == UnidadeFinal:
                posiçãofinal=ListadeUnidades.index(i)
posições= posiçãofinal-posiçãoinicial
Valor2=1024**posições
Valor3= Valor3/Valor2

if UnidadeFinal == unidadebit:
        Valor3 = (Valor/1024)*8

print(f"{Valor3:.14f}")