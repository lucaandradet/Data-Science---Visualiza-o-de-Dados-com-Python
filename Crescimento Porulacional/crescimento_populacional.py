#Crescimento da população brasileira 1980-2016 - DATASUS
import matplotlib.pyplot as plt #importando biblioteca matplotlib

dados = open("populacao_brasileira.csv").readlines()

x = [] #Anos
y = [] #População

for i in range(len(dados)): #Percorrendo dados
    if i != 0: #Desprezando a linha zero
        linha = dados[i].split(';') #Quebra dados em duas céluas
        x.append(int(linha[0])) #captura o valor do ano
        y.append(int(linha[1])) #captura o valor da população

plt.bar(x,y, color='#e4e4e4')
plt.plot(x,y, color="k",linestyle="--")

plt.title("Crescimento da população brasileira 1980-2016")
plt.xlabel("Ano")
plt.ylabel("População 100 milhões")

plt.savefig("populacao_brasileira.png", dpi=300)
plt.show()