import sympy
from sympy.abc import x, y, z


F  = (x-3)**2 + (y-2)**2
ponto = [3/4, 1/4]

gradiente = [0, 0]
gradiente_em_p = [0, 0]
nova_solucao = [0, 0]
gradiente[0] = F.diff(x)
gradiente[1] = F.diff(y)
i = 0
while(i < 20):
    gradiente_em_p[0] = gradiente[0].subs(x, ponto[0])
    gradiente_em_p[1] = gradiente[1].subs(y, ponto[1])
    nova_solucao[0] = ponto[0] - (z * gradiente_em_p[0])
    nova_solucao[1] = ponto[1] - (z * gradiente_em_p[1])
    Z = F.subs(x, nova_solucao[0])
    Z = Z.subs(y, nova_solucao[1])
    Z = Z.diff(z)
    Z = sympy.solve(Z)
    if type(Z) == list:
        Z = Z[0]
    elif Z == 0:
        print("O ponto otimo foi encontrado em {} execuções".format(i))
        i = 200
    ponto[0] = nova_solucao[0].subs(z, Z)
    ponto[1] = nova_solucao[1].subs(z, Z)
    i+=1
