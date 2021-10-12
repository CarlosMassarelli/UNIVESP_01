import pandas as pd
import numpy as np

df = pd.read_excel(r'tabela_naoh.xlsx', index_col=0)


def concent(temperatura, densidade):
    global concentra

    if temperatura % 2 != 0:
        temperatura += 1

    concentra = df[temperatura]
    resultado = getnearpos(concentra, densidade)
    return resultado  # float


def getnearpos(array, value):
    idx = (np.abs(array-value)).idxmin()
    return idx


temperatura = 26
densidade = 1.2859

print('Função principal :', concent(temperatura, densidade))




# temp = 24
# den = 1.2867
#
#
# # print(x, end='\n\n\n')
# # print(coluna, end='\n\n\n')
# # print(elemento, end='\n\n\n')
# # print(elemento.index, end='\n\n\n')
# # print(elemento.index[0], end='\n\n\n')
# print(x, end='\n\n\n')
#
#
# # Forma 01
# coluna = x[x[temp] == den]
# elemento = coluna[temp]
# naoh = elemento.index[0]
# print(naoh, end='\n\n\n')
# # print(x.index)
#
# # Forma 02
# sel = x[temp] == den
# print(x[sel].index[0], end='\n\n\n')
#
# # Forma 03
# teste = x.loc[x[temp] == den]
# print(teste.index[0])
