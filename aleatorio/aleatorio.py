import sympy
import random
import matplotlib.pyplot as plt
from sympy.abc import x, y, alpha
import numpy as np

#inicaliza as variáveis
alcance = [-1 , 1] # range do número aleatório
dk = [0, 0] # incialização da lista 
X = [ 0, 0] # X = x0 + alpha * dk
function = x**2 + y**2 -300 # a função em sí
ini = [50, 100] # ponto inicial
valor_no_ponto = [3, 2] 
plotX = [] # eixo X
plotY = [] # eixo Y
vetor = [] # vetor de Comparação


def Criterio(vetor,valor):

    valores = [0,0,0,0,0]
    vetor.append(valor)
 
    if(len(vetor)>=5):
        delta= max(vetor)-min(vetor)
        for i in range(5): # copia os últimos 5 elementos para um auxiliar 
            valores[i] = vetor[-(i+1)]
        dround = max(valores)-min(valores)
        if(dround <= 0.000001*delta):
            return 1
    return 0

def optimize(a, b):
    i = 0
    solucao = 1
    while (i < 100 ):
        # printa a iteração
        print("+++++++++ ITERAÇÃO {} +++++++++".format(i))
        # inicializa as variáveis aleatŕoiamente 
        dk[0] = random.uniform(alcance[0], alcance[1])
        dk[1] = random.uniform(alcance[0], alcance[1])
        print(dk)
        # as aplica na função objetivo
        # aplica xk + aplhak *  dk
        X[0] = ini[0] + alpha * dk[0]
        X[1] = ini[1] + alpha * dk[1]
        # aplica X na função f
        alpha_k = function.subs( x, X[0])
        alpha_k = alpha_k.subs(y, X[1])
        # deriva a função alpha_K achando seu ponto de máximo
        alpha_k = alpha_k.diff( alpha )
        # resolver alpha
        solucao = sympy.solve( alpha_k, alpha)
        #import pdb; pdb.set_trace()
        ini[0] = X[0].subs(alpha, solucao[0])
        ini[1] = X[1].subs(alpha, solucao[0])
        # gera o valor final de F aplicado nos pontos
        final = function.subs( x, ini[0])
        final = final.subs(y, ini[1])
        # printa as soluções no terminal
        print("solução de iteração {} é {} com os pontos: ({}, {})".format(i, solucao, ini[0], ini[1]))
        # adiciona para plotagem
        plotX.append(final)
        print("----------------- Valor Final") 
        print(final)	
        if(Criterio( vetor, final )==1):
            break

        i += 1
    
    

    plt.plot(plotX, 'ro')
    plt.show()

if __name__ == "__main__":
    print("Iremos Otimizar a função F(x) = {}".format(function))
    optimize(valor_no_ponto[0], valor_no_ponto[1])
