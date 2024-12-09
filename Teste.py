import pandas as pd

tabela = pd.DataFrame({"Nome":["Lira","Fabrico"], "Idade": [29,25]})
print(tabela)

for i in range(0,27):
    if i % 2 == 0:
        print(i)