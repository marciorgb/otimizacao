import sympy
import matplotlib.pyplot as plt
from sympy.abc import x, y, alpha


F = (x + 2*y -7)**2 + (2*x + y - 5)**2
ponto = [-150, 250]

gradiente = [0, 0]
dk = [0, 0]
X = [0, 0]
gradiente[0] = F.diff(x)
gradiente[1] = F.diff(y)
i = 0
solucao = 1
plotX = []
plotY = []
vetor = []

def Criterio(vetor,valor):

    valores = [0,0,0,0,0]
    vetor.append(valor)

    if(len(vetor)>=5):
        delta= max(vetor)-min(vetor)
        for i in range(5):
            valores[i] = vetor[-(i+1)]
        dround = max(valores)-min(valores)
        if(dround <= 0.0000001*delta):
            return 1
    return 0

print("O gradiente é")
print(gradiente[0])
print(gradiente[1])
while(i < 10000):
    print("++++++++ ITERAÇÃO {} ++++++++".format(i))
    # gradiente em p0
    dk[0] = gradiente[0].subs(x, ponto[0])
    dk[0] = dk[0].subs(y, ponto[1])
    # gradiente em p1
    dk[1] = gradiente[1].subs(x, ponto[0])
    dk[1] = dk[1].subs(y, ponto[1])
    # soluções X
    X[0] = ponto[0] - (alpha * dk[0])
    X[1] = ponto[1] - (alpha * dk[1])
    
    alpha_k = F.subs(x, X[0])
    alpha_k = alpha_k.subs(y, X[1])
    
    alpha_k = alpha_k.diff(alpha)
    solucao = sympy.solve(alpha_k, alpha)
    if solucao == []:
        solucao.append(0)
    
    ponto[0] = X[0].subs(alpha, solucao[0])
    ponto[1] = X[1].subs(alpha, solucao[0])
    print("O passo da iteração {} é {}, sendo os pontos P{}({},{})".format(i, solucao[0], i,ponto[0], ponto[1]))
    final = F.subs(x, ponto[0])
    final = final.subs(y, ponto[1])
    print("O valor da solução no ponto P{} é igual {}".format( i , final))
    plotX.append(final)
    if(Criterio(vetor,final)==1):
        break
    i+=1

plt.plot(plotX, 'ro')
plt.show()

print("O ponto otimo foi encontrado em {} execuções".format(i))
