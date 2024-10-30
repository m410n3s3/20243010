
def map():
    def aprovar_pessoa(nome):
        return nome+" APROVADO"

    nomes = ["Larissa", "Rafael", "Marcos","Joao"]
    # print(nomes)
    # for i in range(len(nomes)):
    #     nomes[i] = aprovar_pessoa(nomes[i])
    # print(nomes)


    # Nomes_Aprovados = []
    # for i in range(len(nomes)):
    #     Nomes_Aprovados.append(aprovar_pessoa(nomes[i]))
    # print(nomes)

    situacao = list(map(aprovar_pessoa,nomes))
    print(situacao)
    print(nomes)

    nomes = list(map(aprovar_pessoa,nomes))
    print(nomes)

# def map2():
#     # A = input("Entre com uma quantidade de numeros: ").split()
#     # print(A)
#     # A = list(map(int, ["1", "2"]))
#     # print(A)
    



def filter_map():
    pinturas = [
        ['Picasso', 'Les demoiselles', 1907],
        ['Monet', "Lagoa dos lirios d'água", 1899],
        ['Renoir', "Duas irmãs",1881],
        ['Tarcila', 'Abaporu', 1928] ]
    def antiguidade(pintura):
        if pintura[2]<1900:
            return True
        else:
            return False
    print("Filter")
    print(list(filter(antiguidade, pinturas)))
    # print("Map")
    # print(list(map(antiguidade, pinturas)))

def set():
    numeros = [2,2,5,8] #O número 2 aparece duplicado
    # set_numeros = set(numeros) #Pode alterar a ordenação original.
    print(numeros)

    a = {2,2,5,8}
    b = {2,2,3,9}
    print(a.intersection(b))
    print(a.symmetric_difference(b))
    print(a.union(b))
    print(b.intersection(a))

if __name__=="__main__":
    set()
