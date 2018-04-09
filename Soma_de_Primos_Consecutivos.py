'''
    Soma de Números Primos Consecutivos
    
    Enunciado: Qual é o número primo, abaixo de um milhão, 
    que pode ser escrito como a soma da maior quantidade de números primos?
    
    Exemplo com limitante em 100: Dos primos compostos só pela soma de outros números primos, 
    41 é o que exige a maior quantidade de somas abaixo de 100. 
    41 = 2 + 3 + 5 + 7 + 11 + 13
'''

from sympy import sieve, isprime

# limitante superior
mx = 1000000

# lista de primos
P = [i for i in sieve.primerange(2, mx)]
# S: agiliza busca com in
# Pc: lista acumulativa de primos
S, Pc = set(P), [2]

# monta lista acumulativa
for i in P[1:]:
	# se a soma atingir mx, 
	# já passou da resposta
	# e pode sair do for
        if Pc[-1]+i >= mx:
                break
	# do contrário, adiciona
        Pc.append(Pc[-1] + i)

# cnt: counter das adições
# p: primo das cnt somas
cnt, p = 0, None

# caso 2 esteja na solução
# vai das maiores somas às menores
# pra sair do for o quanto antes
for i in Pc[::-1]:
	# se i é primo, tá no intervalo
	# e maximiza quantidade de somas
        if i in S and Pc.index(i)+1 > cnt:
		# atualiza counter
		# e o primo correspondente
                cnt, p = Pc.index(i)+1, i
                break

# caso 2 não esteja na solução
for i in range(1, len(Pc)):
	# vai das maiores somas às menores
	# pra sair do for o quanto antes
        for j in range(len(Pc)-1, i, -1):
		# se maximiza quantidade de somas
		# e é um primo no intervalo
                if j-i+1 > cnt and (Pc[j] - Pc[i-1]) in S:
			# atualiza counter
			# e o primo correspondente
                        cnt, p = j-i+1, Pc[j]-Pc[i-1]
                        break

print('Resposta:', p)
