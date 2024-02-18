from random import randint

def main():
    #Criação do vetor com tamanho desejado e com inteiros aleatórios
    tamanho = input('Tamanho do Vetor: ')
    tamanho = int(tamanho)
    vet = []
    for i in range(tamanho):
        vet.append(randint(1, tamanho))

    #Bubble sort
    for i in range(tamanho-1):
        for j in range(tamanho-1-i):
            #Troca posição do vet com a do próximo, caso o proximo seja menor que o atual
            if vet[j]>vet[j+1]:
                aux=vet[j+1]
                vet[j+1]=vet[j]
                vet[j]=aux

    print(vet[i])

if __name__ == "__main__":
    main()
