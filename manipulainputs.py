#Manipula Inputs 1.0
#Recebe um input do usuário e manipula como ele quiser
def manipula(entrada,m):
    if entrada:
        if m == 0: return entrada
        elif m == 1: return entrada.title()
        else:
            return entrada.upper()
        
    #if entrada == 'pedro prata' and m == 2: return 'PEDRO PRATA'
    #if entrada == 'pedro prata' and m == 1: return 'Pedro Prata'
    #if entrada and m == 0: return entrada

#testes
assert manipula('pedro',0) == 'pedro'
assert manipula('minha entrada', 0) == 'minha entrada'
assert manipula('pedro prata',1) == 'Pedro Prata'
assert manipula('pedro prata', 2) == 'PEDRO PRATA'
assert manipula('joão lucas',10) == 'JOÃO LUCAS'