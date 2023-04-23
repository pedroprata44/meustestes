#Recebe duas strings e retorna
#Separa uma da outra por um espaço
def inputoutput(input1,input2):
    s, s2 = str(input1), str(input2)

    if s and s2: return ' '.join((s,s2))
    elif s or s2: return 'Uma das strings estão vazias'
    else:
        return 'As strings estão vazias'

#teste
assert inputoutput('Pedro', '') == 'Uma das strings estão vazias'
assert inputoutput('','') == 'As strings estão vazias'
assert inputoutput('Pedro', 'Prata') == 'Pedro Prata'
assert inputoutput('João', 'Lucas') == 'João Lucas'
assert inputoutput(10,20) == '10 20'
assert inputoutput(10.435342563425, 280342597423.112345)