import sympy
import random
import matplotlib.pyplot as plt
from sympy.abc import x, y, alpha

#inicaliza as variáveis
alcance = [-1 , 1]
dk = [0, 0]
X = [ 0, 0]
function = x**2 +y**2
ini = [-3, 2]
valor_no_ponto = [3, 2]
plotX = []
plotY = []

def optimize(a, b):
    i = 0
    while ( i <10 ):
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
        final = function.subs( x, ini[0])
        final = final.subs(y, ini[1])
        # printa as soluções no terminal
        print("solução de iteração {} é {} com os pontos: ({}, {})".format(i, solucao, ini[0], ini[1]))
        # itera o i
        plotX.append(ini[0])
        plotY.append(ini[1])
        i += 1
    plt.plot(plotX, plotY, 'ro')
    plt.show()

if __name__ == "__main__":
    #alcance[0] = input("Insira o range de aletoriedade [-1,1](um valor por vez):")
    #alcance[1] = input()
    #function = sympy.simplify(input("Insira a equação objetivo [x**2 + y**2]"))
    #ini[0] = input("Insira o valor do ponto [ -3, 2]")
    #ini[1] = input()
    print("Iremos Otimizar a função F(x) = {}".format(function))
    optimize(valor_no_ponto[0], valor_no_ponto[1])
