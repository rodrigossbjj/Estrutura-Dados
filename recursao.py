# LISTA 1

# 1. Para cada uma das operações abaixo, forneça o tempo de execução usando a notação O grande
# a. O(n)
# b. O(Logn)
# c. O(n^2)
# d. O(n)
# e. O(n^2)

# 2. Coloque as funções abaixo em ordem crescente de complexidade assintótica
# a. 100(logn)^3, 10n(logn)^2, n^3, 2^n
# b. 300nlogn, 10^4n^2, 10^(-2)2^n
# c. 2n, 10^2nlogn, 10^2n^2, 100n^3
# d. 2^10, 4n, nlogn, 4nlogn + 2n, n^2+10n, n^3

# 3. Marque V ou F, considerando que:
    # f(n) = 5000n2+800nlogn
    # g(n)=90n3+900n2+9000n+90000
    # h(n) = 20logn + 100n+ n2
# (V) g(n) = O(f(n))
# (V) g(n) = 𝛀(h(n))
# (V) g(n) = θ(f(n))


# 6. Determine a complexidade dos trechos de código abaixo:
# a. N
# b. N^2 
# c. N

# LISTA 2


# # QUESTÃO 1
# Projete um algoritmo recursivo para determinar o maior elemento em uma sequência de inteiros S com n elementos

def maiorNum(s):
    if len(s) == 1:
        return s[0]
    
    maior = maiorNum(s[1:])

    if s[0] > maior:
        return s[0]
    
    return maior
    

# QUESTÃO 3
# Escreva um algoritmo recursivo que organize uma sequência de inteiros de tal forma que os valores pares apareçam antes do que os ímpares.
def organizaSeq(aS, pS=[], iS=[]):
    if len(aS) == 0:
        return pS + iS
    if aS[0]%2==0:
        return organizaSeq(aS[1:], pS + [aS[0]], iS)
    return organizaSeq(aS[1:], pS, iS+ [aS[0]])


# Escreva as funções recursivas listas a seguir, todas recebem um inteiro e devolvem um inteiro.
# a.maiorDigito
#   retorna o maior dígito de um inteiro
def maiorDigito(n):
    if n < 10:
        return n
    if n%10 < maiorDigito(n//10):
        return maiorDigito(n//10)
    return n%10

# b.menorDigito
#   retorna o menor dígito de um inteiro
def menorDigito(n):
    if n < 10:
        return n
    if n%10 > menorDigito(n//10):
        return menorDigito(n//10)
    return n%10

# contaDigito
#   c.retorna a quantidade de dígitos de um inteiro
def contaDigito(n):
    if n < 10:
        return 1
    return 1 + contaDigito(n//10)

# somaDigito
#   d.retorna a soma dos dígitos de um inteiro
def somaDigito(n):
    if n < 10:
        return n
    return n%10 + somaDigito(n//10)

# zeraPares
#   e.retorna um inteiro com os dígitos pares em zero
def zeraPares(n): 
    if n < 10:
        if n%2==0:
            return 0
        return n
    
    return zeraPares(n//10) * 10 + zeraPares(n%10)

# zeraImpares
#   f.retorna um inteiro com os dígitos ímpares em zero
def zeraImpares(n):
    if n < 10:
        if n%2==0:
            return n
        return 0
    
    return zeraImpares(n//10) * 10 + zeraImpares(n%10)

# removePares
#   g.remove os dígitos pares de um inteiro
def removePares(n): 
    if n < 10:
        if n%2==0:
            return 0
        return n
    
    if (n%10) % 2 == 0:
        return removePares(n // 10)
    else:
        return removePares(n // 10) * 10 + (n%10)

# removeImpares
#   h.remove os dígitos ímpares de um inteiro
def removeImpares(n): 
    if n < 10:
        if n%2!=0:
            return 0
        return n

    if (n%10) % 2 != 0:
        return removeImpares(n // 10)
    else:
        return removeImpares(n // 10) * 10 + (n%10)


# QUESTÃO 6
# Crie uma função recursiva para verificar se uma string tem mais vogais do que consoantes.
def contaVogais(p, countVogais, countConsoantes):
    vogais = ['a','e','i','o','u']
    if len(p) == 0:
        if countVogais > countConsoantes:
            return ("Mais vogais")
        else:
            return ("Mais consoantes")        

    if p[0] in vogais:
        return contaVogais(p[1:], countVogais + 1, countConsoantes)
    return contaVogais(p[1:], countVogais, countConsoantes + 1)    

print(maiorNum([10, 3, 7, 1]))



def main():
    print(removeImpares(53465))


if __name__ == "__main__":
    main()
