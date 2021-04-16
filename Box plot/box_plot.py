#Box plot - diagrama de caixa
import matplotlib.pyplot as plt #importando biblioteca matplotlib
import random #importando biblioteca random

vetor = [] #Criando vetor vazio

for i in range(10): #For de i até 10
    numero_aleatorio = random.randint(0,1000) #Aonde gera um número aleatório de 0 a 1000
    vetor.append(numero_aleatorio) #Adiciona esse número aleatório ao vetor

plt.boxplot(vetor) #Definindo o vetor como boxplot
plt.title("Boxplot") #Título do gráfico
plt.show() #Criando Gráfico