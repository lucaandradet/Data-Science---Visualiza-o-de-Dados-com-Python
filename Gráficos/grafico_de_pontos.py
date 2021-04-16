#Visualização de dados em Python
import matplotlib.pyplot as plt #Importando biblioteca matplotlib

x = [1,2,3,4,5] #Definindo pontos no eixo x
y = [2,3,7,1,4] #Definindo pontos no eixo y
z = [100,200,300,250,400] #Alterando o tamanho dos circulos

#Python
titulo = "Gráfico de Scatterplot (pontos ou dispersão)" #Definindo Título do gráfico
eixox = "Eixo X" #Definindo título do eixo x
eixoy = "Eixo Y" #Definindo título do eixo y

#Legendas
plt.title(titulo) #Adicionando título dentro da função title
plt.xlabel(eixox) #Adicionando título do eixo x dentro da função xlabel
plt.ylabel(eixoy) #Adicionando título do eixo y dentro da função ylabel

plt.plot(x,y, color="k", linestyle="-.") #Plotando linhas do eixo x e y
plt.scatter(x,y, label="Meus pontos", color='k', marker=".", s=z) #Plotando pontos do eixo x e y
plt.legend() #Plotando legenda definida no label
plt.show() #Exibe gráfico

plt.savefig("figura1.png", dpi=300) #Salvando imagem do plot. DPI - Definindo qualidade da imagem
plt.savefig("figura2.pdf") #Salvando imagem do plot

'''
Documentação oficial do Matplotlib
A seguir, alguns exemplos de argumentos que podem ser aplicados ao método plot( ).

color: cor (ver exemplos abaixo)
label: rótulo
linestyle: estilo de linha (ver exemplos abaixo)
linewidth: largura da linha
marker: marcador (ver exemplos abaixo)

CORES (color)
'b' blue
'g' green
'r' red
'c' cyan
'm' magenta
'y' yellow
'k' black
'w' white

Marcadores (marker)
'.' point marker
',' pixel marker
'o' circle marker
'v' triangle_down marker
'^' triangle_up marker
'<' triangle_left marker
'>' triangle_right marker
'1' tri_down marker
'2' tri_up marker
'3' tri_left marker
'4' tri_right marker
's' square marker
'p' pentagon marker
'*' star marker
'h' hexagon1 marker
'H' hexagon2 marker
'+' plus marker
'x' x marker
'D' diamond marker
'd' thin_diamond marker
'|' vline marker
'_' hline marker

Tipos de linha (linestyle)
'-' solid line style
'--' dashed line style
'-.' dash-dot line style
':' dotted line style

Fonte: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
'''